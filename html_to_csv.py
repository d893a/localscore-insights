''' Iterate over all local html files and extract tables in csv format, using
    TAB as separator. Save result into a single csv file.'''
import re
import csv
import glob
from dateutil import parser as date_parser
from typing import Tuple
from bs4 import BeautifulSoup

def extract_test_num_and_date(ext_el):
    """Extract test number and date from the card element"""
    div = ext_el.find('div', class_='flex flex-col justify-between pb-1')
    if not div:
        return '', ''
    test_num_el = div.find('a', href=re.compile(r'/result/\d+'))
    test_num = test_num_el.text.strip().replace('Test #', '') if test_num_el else ''
    date_el = div.find('p', class_='text-sm text-gray-600 font-light')
    test_date = date_el.text.strip() if date_el else ''
    test_date = normalize_date(test_date)
    return test_num, test_date

def normalize_date(date_str: str) -> str:
    """ Convert date from '07/14/2025 - 1:28 PM' format to 'YYYY.MM.DD HH:MM:SS'"""
    try:
        dt = date_parser.parse(date_str)
        return dt.strftime('%Y.%m.%d %H:%M:%S')
    except ValueError:
        return date_str  # Return original if parsing fails

def extract_accelerator_info(ext_el) -> Tuple[str, str, str, str]:
    """Extract accelerator, accelerator type, and memory from the card element"""
    ext_el = ext_el.find('div', class_='grid grid-cols-12 w-full items-center gap-2')
    accel_el = ext_el.find('a', href=re.compile(r'/accelerator/\d+'))
    accel_name = accel_el.text.strip() if accel_el else ''
    accel_type_el = ext_el.find('div', class_='md:text-sm text-xs font-light sm:-mt-1')
    accel_type = accel_type_el.text.strip() if accel_type_el else ''
    accel_ram, accel_ram_unit = extract_accel_ram(ext_el)
    return accel_name, accel_type, accel_ram, accel_ram_unit

def extract_accel_ram(ext_el) -> Tuple[str, str]:
    """Extract memory size value and unit from the card element"""
    el = ext_el.find_all('div', class_='flex flex-col justify-center col-span-2')
    accel_ram = el[0].text.strip() if el else ''
    accel_ram, accel_ram_unit = normalize_ram(accel_ram)
    return accel_ram, accel_ram_unit

def extract_model_name_quant_params(ext_el) -> Tuple[str, str, str, str]:
    """Extract model name and bits from the card element"""
    el = ext_el.find('div', class_='grid grid-cols-12 w-full items-center gap-2 h-full')
    if not el:
        return '', '', '', ''
    model_name, quant = extract_model_name_quant(el)
    params, params_unit = extract_model_params(el)
    return model_name, quant, params, params_unit

def extract_model_name_quant(ext_el) -> Tuple[str, str]:
    """Extract model name and quantization"""
    el = ext_el.find('a', href=re.compile(r'/model/\d+'))
    if not el:
        return '', ''
    model_el = el.find('p', class_='font-medium md:text-base text-sm')
    model_name = model_el.text.strip() if model_el else ''
    quant_p = el.find('p', class_='sm:-mt-1 md:text-sm text-xs')
    quant = quant_p.text.strip() if quant_p else ''
    return model_name, quant

def extract_model_params(ext_el) -> Tuple[str, str]:
    """Extract model params value"""
    params_el = ext_el.find('div', class_='flex flex-col justify-center col-span-2')
    params_val_unit_el = params_el.find('span', class_='font-medium md:text-base text-sm')
    params_val = params_val_unit_el.text.strip() if params_val_unit_el else ''
    params_unit = ''
    if params_val.endswith('B'):
        params_val = f"{int(float(params_val[:-1]) * 1000)}"
        params_unit = 'M'
    elif params_val.endswith('M'):
        params_val = params_val[:-1]
        params_unit = 'M'
    return params_val, params_unit

def extract_perf_metrics(ext_el) -> Tuple[str, str, str, str, str]:
    """Extract performance metrics from the card element"""
    perf_el = ext_el.find('div', class_='grid items-center grid-cols-2 sm:gap-2 gap-x-16 gap-y-2 col-span-6 self-center sm:self-auto')
    if not perf_el:
        return '', '', '', '', ''
    metrics_els = perf_el.find_all('div', class_='flex flex-col items-center sm:gap-0')
    gen_tps = ttft = ttft_unit = prompt_tps = localscore = ''
    for i, metric_el in enumerate(metrics_els):
        match i:
            case 0:  # generation TPS
                gen_tps, _ = extract_metrics_unit(metric_el)
                gen_tps = f"{float(gen_tps):.1f}" if gen_tps else ''
            case 1:  # time to first token
                ttft, ttft_unit = extract_metrics_unit(metric_el)
            case 2:  # prompt
                prompt_tps, _ = extract_metrics_unit(metric_el)
            case 3:  # LocalScore
                localscore, _ = extract_metrics_unit(metric_el)
    ttft, ttft_unit = normalize_ttft(ttft, ttft_unit)
    return gen_tps, ttft, ttft_unit, prompt_tps, localscore

def normalize_ttft(ttft: str, ttft_unit: str) -> Tuple[str, str]:
    """Normalize ttft time to milliseconds"""
    if ttft_unit == "sec":
        ttft = str(int(float(ttft) * 1000))
        ttft_unit = 'ms'
    return ttft, ttft_unit

def extract_metrics_unit(ext_el) -> Tuple[str, str]:
    """Extract generation TPS and time to first token"""
    val_el = ext_el.find('p', class_='font-medium text-lg') if ext_el else None
    val = val_el.text.strip() if val_el else ''
    unit_el = ext_el.find('p', class_='text-xs font-light') if ext_el else None
    unit = unit_el.text.strip() if unit_el else ''
    return val, unit

def extract_system_info(ext_el) -> Tuple[str, str, str, str]:
    """Extract system information from the card element"""
    system_el = ext_el.find('div', class_='grid grid-cols-5 gap-1 text-xs sm:text-sm mt-2')
    cpu = ram = ram_unit = os_name = ''
    if not system_el:
        return '', '', '', ''
    cpu_el = system_el.find('div', class_='md:col-span-3 col-span-5 flex items-center gap-1')
    if cpu_el:
        cpu_spans = cpu_el.find_all('div', class_='font-medium')
        cpu = cpu_spans[0].text.strip() if cpu_spans else ''
    ram_el = system_el.find('div', class_='md:col-span-1 col-span-3 flex items-center gap-1')
    if ram_el:
        ram_spans = ram_el.find_all('div', class_='font-medium')
        ram = ram_spans[0].text.strip() if ram_spans else ''
        ram, ram_unit = normalize_ram(ram)
    os_el = system_el.find('div', class_='md:col-span-1 col-span-2 flex items-center gap-1 justify-end')
    if os_el:
        os_spans = os_el.find_all('div', class_='font-medium')
        os_name = os_spans[0].text.strip() if os_spans else ''
    return cpu, ram, ram_unit, os_name

def normalize_ram(ram: str) -> Tuple[str, str]:
    """Normalize RAM size to GB"""
    ram_unit = ''
    if ram.endswith('GB'):
        ram = ram[:-2].strip()
        ram_unit = 'GB'
    elif ram.endswith('TB'):
        ram = str(int(float(ram[:-2]) * 1024))
        ram_unit = 'GB'
    return ram, ram_unit

def extract_test_data_from_html(html_content):
    """Extract test data from HTML content"""
    soup = BeautifulSoup(html_content, 'html.parser')
    test_data = []

    # Find all test result cards
    test_cards = soup.find_all('div', class_="bg-white rounded-md shadow-[0_24px_54px_0_rgba(88,42,203,0.03)] px-5 py-4 flex flex-col")
    print(f"{len(test_cards)} test cards: ", end='')

    for card_index, card in enumerate(test_cards):
        try:
            test_num, test_date = extract_test_num_and_date(card)
            accel_name, accel_type, accel_ram, accel_ram_unit = extract_accelerator_info(card)
            model_name, quant, params, params_unit = extract_model_name_quant_params(card)
            gen_tps, ttft, ttft_unit, prompt_tps, localscore = extract_perf_metrics(card)
            system_cpu, system_ram, system_ram_unit, system_os = extract_system_info(card)

            test_data.append({
                'test_num': test_num,
                'test_date': test_date,
                'gen_tps': gen_tps,
                'ttft': ttft,
                'ttft_unit': ttft_unit,
                'prompt_tps': prompt_tps,
                'localscore': localscore,
                'model_name': model_name,
                'model_quant': quant,
                'model_params': params,
                'model_params_unit': params_unit,
                'accel_name': accel_name,
                'accel_type': accel_type,
                'accel_ram': accel_ram,
                'accel_ram_unit': accel_ram_unit,
                'system_cpu': system_cpu,
                'system_ram': system_ram,
                'system_ram_unit': system_ram_unit,
                'system_os': system_os
            })

        except Exception as e:
            print(f"\n  {card_index}: Error: {e}")
            continue

    return test_data

def main():
    # Get all HTML files in current directory
    html_files = glob.glob('latest_*.html')

    if not html_files:
        print("No HTML files found matching pattern 'latest_*.html'")
        return

    print(f"Found {len(html_files)} HTML files")

    all_data = []

    # Process each HTML file
    for html_file in sorted(html_files):
        print(f"Processing {html_file}: ", end='')
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()

            test_data = extract_test_data_from_html(html_content)
            all_data.extend(test_data)
            print(f" {len(test_data)} test results    ", end='\r')

        except Exception as e:
            print(f"Error processing {html_file}: {e}")
    print()

    all_data.sort(key=lambda x: int(x['test_num']))

    # Write to CSV file
    if all_data:
        output_file = 'localscore_leaderboard.csv'
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = all_data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
            writer.writeheader()
            writer.writerows(all_data)
        print(f"\rSuccessfully extracted {len(all_data)} test results")
        print(f"Data saved to {output_file}")
    else:
        print("No data extracted from HTML files")

if __name__ == "__main__":
    main()
