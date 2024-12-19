import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import time
import re
import random
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')  # 设置标准输出为 UTF-8
sys.stderr.reconfigure(encoding='utf-8')  # 设置标准错误输出为 UTF-8


path = ".\\visa_G" # 用于存放结果的相对位置
os.chdir(path)

# 目标时间点
date =  20190129 #202004 #202105 #20220526 #202307 #202412 201305 #201404 #201509 #201604 #201702 #

# 待收集国家名称
"""
nations = {
    "Afghanistan": ["Afghan", "Afghanistan"],
    "Armenia": ["Armenian", "Armenia"],
    "Australia": ["Australian", "Australia"],
    "Azerbaijan": ["Azerbaijani", "Azerbaijan"],
    "Bahrain": ["Bahraini", "Bahrain"],
    "Bangladesh": ["Bangladeshi", "Bangladesh"],
    "Belarus": ["Belarusian", "Belarus"],
    "Brunei": ["Bruneian", "Brunei"],
    "Cambodia": ["Cambodian", "Cambodia"],
    "China": ["Chinese", "China"],
    "Cyprus": ["Cypriot", "Cyprus"],
    "Estonia": ["Estonian", "Estonia"],
    "Fiji": ["Fijian", "Fiji"],
    "Georgia": ["Georgian", "Georgia"],
    "HongKongSARChina": ["Chinese_citizens_of_Hong_Kong", "Hong Kong"],
    "India": ["Indian", "India"],
    "Indonesia": ["Indonesian", "Indonesia"],
    "Iran": ["Iranian", "Iran"],
    "Iraq": ["Iraqi", "Iraq"],
    "Israel": ["Israeli", "Israel"],
    "Japan": ["Japanese", "Japan"],
    "Jordan": ["Jordanian", "Jordan"],
    "Kazakhstan": ["Kazakhstani", "Kazakhstan"],
    "Kiribati": ["Kiribati", "Kiribati"],
    "Kuwait": ["Kuwaiti", "Kuwait"],
    "Kyrgyzstan": ["Kyrgyzstani", "Kyrgyzstan"],
    "Laos": ["Laotian", "Laos"],
    "Latvia": ["Latvian", "Latvia"],
    "Lebanon": ["Lebanese", "Lebanon"],
    "Lithuania": ["Lithuanian", "Lithuania"],
    "Malaysia": ["Malaysian", "Malaysia"],
    "Moldova": ["Moldovan", "Moldova"],
    "Mongolia": ["Mongolian", "Mongolia"],
    "Myanmar": ["Burmese", "Myanmar"],
    "Nepal": ["Nepalese", "Nepal"],
    "NewZealand": ["New_Zealand", "New Zealand"],
    "Oman": ["Omani", "Oman"],
    "Pakistan": ["Pakistani", "Pakistan"],
    "PapuaNewGuinea": ["Papua_New_Guinean", "Papua New Guinea"],
    "Philippines": ["Filipino", "Philippines"],
    "Qatar": ["Qatari", "Qatar"],
    "Russia": ["Russian", "Russia"],
    "SaudiArabia": ["Saudi", "Saudi Arabia"],
    "Singapore": ["Singaporean", "Singapore"],
    "SriLanka": ["Sri_Lankan", "Sri Lanka"],
    "Tajikistan": ["Tajikistani", "Tajikistan"],
    "Thailand": ["Thai", "Thailand"],
    "Tonga": ["Tongan", "Tonga"],
    "Turkey": ["Turkish", "Turkey"],
    "UnitedArabEmirates": ["Emirati", "United Arab Emirates"],
    "Uzbekistan": ["Uzbekistani", "Uzbekistan"],
    "Vanuatu": ["Vanuatuan", "Vanuatu"],
    "Vietnam": ["Vietnamese", "Vietnam"],
    "Yemen": ["Yemeni", "Yemen"],
    "SouthKorea": ["South_Korean", "South Korea"],
    "Syria": ["Syrian", "Syria"],
    "Bhutan": ["Bhutanese", "Bhutan"]
}
"""

nations = {
    "Afghanistan": "for_Afghan_citizens",
    "Albania": "for_Albanian_citizens",
    "Algeria": "for_Algerian_citizens",
    "Andorra": "for_Andorran_citizens",
    "Angola": "for_Angolan_citizens",
    "Antigua and Barbuda": "for_Antigua_and_Barbuda_citizens",
    "Argentina": "for_Argentine_citizens",
    "Armenia": "for_Armenian_citizens",
    "Australia": "for_Australian_citizens",
    "Austria": "for_Austrian_citizens",
    "Azerbaijan": "for_Azerbaijani_citizens",
    "Bahamas": "for_Bahamian_citizens",
    "Bahrain": "for_Bahraini_citizens",
    "Bangladesh": "for_Bangladeshi_citizens",
    "Barbados": "for_Barbadian_citizens",
    "Belarus": "for_Belarusian_citizens",
    "Belgium": "for_Belgian_citizens",
    "Belize": "for_Belizean_citizens",
    "Benin": "for_Beninese_citizens",
    "Bhutan": "for_Bhutanese_citizens",
    "Bolivia": "for_Bolivian_citizens",
    "Bosnia and Herzegovina": "for_Bosnia_and_Herzegovina_citizens",
    "Botswana": "for_Botswanan_citizens",
    "Brazil": "for_Brazilian_citizens",
    "Brunei": "for_Bruneian_citizens",
    "Bulgaria": "for_Bulgarian_citizens",
    "Burkina Faso": "for_Burkinabe_citizens",
    "Burundi": "for_Burundian_citizens",
    "Cape Verde": "for_Cape_Verdean_citizens",
    "Cambodia": "for_Cambodian_citizens",
    "Cameroon": "for_Cameroonian_citizens",
    "Canada": "for_Canadian_citizens",
    "Central African Republic": "for_Central_African_citizens",
    "Chad": "for_Chadian_citizens",
    "Chile": "for_Chilean_citizens",
    "China": "for_Chinese_citizens",
    "Colombia": "for_Colombian_citizens",
    "Comoros": "for_Comorian_citizens",
    "Democratic Republic of the Congo": "for_Democratic_Republic_of_the_Congo_citizens",
    "Costa Rica": "for_Costa_Rican_citizens",
    "Croatia": "for_Croatian_citizens",
    "Cuba": "for_Cuban_citizens",
    "Cyprus": "for_Cypriot_citizens",
    "Czech Republic": "for_Czech_citizens",
    "Denmark": "for_Danish_citizens",
    "Djibouti": "for_Djiboutian_citizens",
    "Dominica": "for_Dominica_citizens",
    "Dominican Republic": "for_Dominican_Republic_citizens",
    "Ecuador": "for_Ecuadorian_citizens",
    "Egypt": "for_Egyptian_citizens",
    "El Salvador": "for_Salvadoran_citizens",
    "Equatorial Guinea": "for_Equatorial_Guinean_citizens",
    "Eritrea": "for_Eritrean_citizens",
    "Estonia": "for_Estonian_citizens",
    "Eswatini": "for_Swazi_citizens",
    "Ethiopia": "for_Ethiopian_citizens",
    "Fiji": "for_Fijian_citizens",
    "Finland": "for_Finnish_citizens",
    "France": "for_French_citizens",
    "Gabon": "for_Gabonese_citizens",
    "Gambia": "for_Gambian_citizens",
    "Georgia": "for_Georgian_citizens",
    "Germany": "for_German_citizens",
    "Ghana": "for_Ghanaian_citizens",
    "Greece": "for_Greek_citizens",
    "Grenada": "for_Grenadian_citizens",
    "Guatemala": "for_Guatemalan_citizens",
    "Guinea": "for_Guinean_citizens",
    "Guinea-Bissau": "for_Guinea-Bissauan_citizens",
    "Guyana": "for_Guyanese_citizens",
    "Haiti": "for_Haitian_citizens",
    "Honduras": "for_Honduran_citizens",
    "Hong Kong": "for_Chinese_citizens_of_Hong_Kong",
    "Hungary": "for_Hungarian_citizens",
    "Iceland": "for_Icelandic_citizens",
    "India": "for_Indian_citizens",
    "Indonesia": "for_Indonesian_citizens",
    "Iran": "for_Iranian_citizens",
    "Iraq": "for_Iraqi_citizens",
    "Ireland": "for_Irish_citizens",
    "Israel": "for_Israeli_citizens",
    "Italy": "for_Italian_citizens",
    "Jamaica": "for_Jamaican_citizens",
    "Japan": "for_Japanese_citizens",
    "Jordan": "for_Jordanian_citizens",
    "Kazakhstan": "for_Kazakhstani_citizens",
    "Kenya": "for_Kenyan_citizens",
    "Kiribati": "for_Kiribati_citizens",
    "North Korea": "for_North_Korean_citizens",
    "South Korea": "for_South_Korean_citizens",
    "Kuwait": "for_Kuwaiti_citizens",
    "Kyrgyzstan": "for_Kyrgyzstani_citizens",
    "Laos": "for_Laotian_citizens",
    "Latvia": "for_Latvian_citizens",
    "Lebanon": "for_Lebanese_citizens",
    "Lesotho": "for_Lesotho_citizens",
    "Liberia": "for_Liberian_citizens",
    "Libya": "for_Libyan_citizens",
    "Liechtenstein": "for_Liechtensteiner_citizens",
    "Lithuania": "for_Lithuanian_citizens",
    "Luxembourg": "for_citizens_of_Luxembourg",
    "Madagascar": "for_Malagasy_citizens",
    "Malawi": "for_Malawian_citizens",
    "Malaysia": "for_Malaysian_citizens",
    "Maldives": "for_Maldivian_citizens",
    "Mali": "for_Malian_citizens",
    "Malta": "for_Maltese_citizens",
    "Marshall Islands": "for_Marshallese_citizens",
    "Mauritania": "for_Mauritanian_citizens",
    "Mauritius": "for_Mauritian_citizens",
    "Mexico": "for_Mexican_citizens",
    "Micronesia": "for_Micronesian_citizens",
    "Moldova": "for_Moldovan_citizens",
    "Monaco": "for_Monégasque_citizens",
    "Mongolia": "for_Mongolian_citizens",
    "Montenegro": "for_Montenegrin_citizens",
    "Morocco": "for_Moroccan_citizens",
    "Mozambique": "for_Mozambican_citizens",
    "Myanmar": "for_Myanmar_citizens",
    "Namibia": "for_Namibian_citizens",
    "Nauru": "for_Nauruan_citizens",
    "Nepal": "for_Nepalese_citizens",
    "Netherlands": "for_Dutch_citizens",
    "New Zealand": "for_New_Zealand_citizens",
    "Nicaragua": "for_Nicaraguan_citizens",
    "Niger": "for_Nigerien_citizens",
    "Nigeria": "for_Nigerian_citizens",
    "North Macedonia": "for_Macedonian_citizens",
    "Norway": "for_Norwegian_citizens",
    "Oman": "for_Omani_citizens",
    "Pakistan": "for_Pakistani_citizens",
    "Palau": "for_Palauan_citizens",
    "Palestine": "for_Palestinian_citizens",
    "Panama": "for_Panamanian_citizens",
    "Papua New Guinea": "for_Papua_New_Guinean_citizens",
    "Paraguay": "for_Paraguayan_citizens",
    "Peru": "for_Peruvian_citizens",
    "Philippines": "for_Filipino_citizens",
    "Poland": "for_Polish_citizens",
    "Portugal": "for_Portuguese_citizens",
    "Qatar": "for_Qatari_citizens",
    "Romania": "for_Romanian_citizens",
    "Russia": "for_Russian_citizens",
    "Rwanda": "for_Rwandan_citizens",
    "Saint Kitts and Nevis": "for_Saint_Kitts_and_Nevis_citizens",
    "Saint Lucia": "for_Saint_Lucian_citizens",
    "Saint Vincent and the Grenadines": "for_Saint_Vincent_and_the_Grenadines_citizens",
    "Samoa": "for_Samoan_citizens",
    "San Marino": "for_Sammarinese_citizens",
    "São Tomé and Príncipe": "for_Santomean_citizens",
    "Saudi Arabia": "for_Saudi_citizens",
    "Senegal": "for_Senegalese_citizens",
    "Serbia": "for_Serbian_citizens",
    "Seychelles": "for_Seychellois_citizens",
    "Sierra Leone": "for_Sierra_Leonean_citizens",
    "Singapore": "for_Singaporean_citizens",
    "Slovakia": "for_Slovak_citizens",
    "Slovenia": "for_Slovenian_citizens",
    "Solomon Islands": "for_Solomon_Islands_citizens",
    "Somalia": "for_Somali_citizens",
    "South Africa": "for_South_African_citizens",
    "Spain": "for_Spanish_citizens",
    "Sri Lanka": "for_Sri_Lankan_citizens",
    "Sudan": "for_Sudanese_citizens",
    "Suriname": "for_Surinamese_citizens",
    "Sweden": "for_Swedish_citizens",
    "Switzerland": "for_Swiss_citizens",
    "Syria": "for_Syrian_citizens",
    "Tajikistan": "for_Tajikistani_citizens",
    "Tanzania": "for_Tanzanian_citizens",
    "Thailand": "for_Thai_citizens",
    "Timor-Leste": "for_East_Timorese_citizens",
    "Togo": "for_Togolese_citizens",
    "Tonga": "for_Tongan_citizens",
    "Trinidad and Tobago": "for_Trinidad_and_Tobago_citizens",
    "Tunisia": "for_Tunisian_citizens",
    "Turkey": "for_Turkish_citizens",
    "Turkmenistan": "for_Turkmen_citizens",
    "Tuvalu": "for_Tuvaluan_citizens",
    "Uganda": "for_Ugandan_citizens",
    "Ukraine": "for_Ukrainian_citizens",
    "United Arab Emirates": "for_Emirati_citizens",
    "United Kingdom": "for_British_citizens",
    "United States": "for_American_citizens",
    "Uruguay": "for_Uruguayan_citizens",
    "Uzbekistan": "for_Uzbekistani_citizens",
    "Vanuatu": "for_Vanuatuan_citizens",
    "Vatican City": "for_Vatican_citizens",
    "Venezuela": "for_Venezuelan_citizens",
    "Vietnam": "for_Vietnamese_citizens",
    "Yemen": "for_Yemeni_citizens",
    "Zambia": "for_Zambian_citizens",
    "Zimbabwe": "for_Zimbabwean_citizens"
}

european_union_countries = [
    'Austria', 
    'Belgium', 
    'Bulgaria', 
    'Croatia', 
    'Cyprus', 
    'Czechia', 
    'Denmark', 
    'Estonia', 
    'Finland', 
    'France', 
    'Germany', 
    'Greece', 
    'Hungary', 
    'Ireland', 
    'Italy', 
    'Latvia', 
    'Lithuania', 
    'Luxembourg', 
    'Malta', 
    'Netherlands', 
    'Poland', 
    'Portugal', 
    'Romania', 
    'Slovakia', 
    'Slovenia', 
    'Spain', 
    'Sweden',
    'United Kingdom'
]

schengen_area_countries = [
    "Austria",
    "Belgium",
    "Bulgaria",
    "Croatia",
    "Czech Republic",
    "Denmark",
    "Estonia",
    "Finland",
    "France",
    "Germany",
    "Greece",
    "Hungary",
    "Iceland",
    "Italy",
    "Latvia",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Malta",
    "Netherlands",
    "Norway",
    "Poland",
    "Portugal",
    "Romania",
    "Slovakia",
    "Slovenia",
    "Spain",
    "Sweden",
    "Switzerland"
]

# 申根区变化
if int(str(date)[:6]) < 202404:
    schengen_area_countries.remove("Bulgaria")
    schengen_area_countries.remove("Romania")
    if int(str(date)[:6]) < 202301:
        schengen_area_countries.remove("Croatia")

# 欧盟变化
if int(str(date)[:6]) > 202002:
    european_union_countries.remove('United Kingdom')


# 创建反向字典用于从官方名字到自己设定的国家名字
# name_to_key = {value[1]: key for key, value in nations.items()}

nations_list = list(nations.keys())

# save_result_dict字典用于保存57个国家分别的被免签政策
save_result_dict = {}

# 定义获取免签国家列表的函数
def fetch_visa_free_countries(country, citizen_name):
    
    countries_visa_policy = [[], [], []] # 分别存放Visa not required; Visa on arrival; eVisa的country
    url = f"https://web.archive.org/web/{date}/https://en.wikipedia.org/wiki/Visa_requirements_{citizen_name}"

    headers_list = [
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
    },
    {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "en-GB,en;q=0.8",
        "Connection": "keep-alive",
    },
    {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Accept-Language": "fr-FR,fr;q=0.7",
        "Connection": "keep-alive",
    },
    {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
        "Accept-Language": "es-ES,es;q=0.6",
        "Connection": "keep-alive",
    },
    {
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/537.36",
        "Accept-Language": "zh-CN,zh;q=0.5",
        "Connection": "keep-alive",
    },
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Accept-Language": "de-DE,de;q=0.9",
        "Connection": "keep-alive",
    },
]

    # 随机选择一个 headers 使用
    headers = random.choice(headers_list)

    try:
        response = requests.get(url, headers=headers, timeout=20)
        if response.status_code == 200:
            print(f"Fetching {country} successfully")
        soup = BeautifulSoup(response.text, 'html.parser')


        # 从无序列表中爬取信息
        # 查找所有无序列表
        ul_elements = soup.find_all('ul')
        # 遍历每个无序列表
        for ul in ul_elements:
            # 遍历每个列表项
            for li in ul.find_all('li'):
                if not li.find('img'):
                    continue  # 如果没有 <img> 标签，则跳过该 <li>，用于剔除wiki页面结尾的噪音数据
                # 查找国家名
                country_name = li.find('a')
                country_name = country_name.text.strip() if country_name else None; country_name = 'Eswatini' if country_name == 'Swaziland' else country_name
                # 提取免签信息文本
                visa_state = li.get_text(separator=" ", strip=True)
                # 添加到结果中
                if country_name in G.columns and country_name != 'Romania':
                    print(f"{country_name} | {visa_state}")
                    # 分类匹配
                    if "arriv" in visa_state.lower() or "voa" in visa_state.lower():
                        countries_visa_policy[1].append(country_name)
                    elif "evisa" in visa_state.lower() or "eta" in visa_state.lower() or "electron" in visa_state.lower() or "online" in visa_state.lower(): 
                        countries_visa_policy[2].append(country_name)
                    else:
                        countries_visa_policy[0].append(country_name)

                    # 欧盟
                    if country_name == "European Union":
                        for i in european_union_countries:
                            countries_visa_policy[0].append(i)
                    
                    if country_name == "Schengen Area":
                        for i in schengen_area_countries:
                            countries_visa_policy[0].append(i)


        # 从免签列表中爬取信息：找到免签列表（通常在页面的表格中）
        visa_tables = soup.find_all('table', {'class': 'wikitable'})
        # 遍历找到的所有表格
        for table_idx, visa_table in enumerate(visa_tables):
            print(f"Processing table {table_idx + 1} ...")
            if not visa_table:                         # 跳过空表格
                continue

            for row in visa_table.find_all('tr')[1:]:  # 跳过表头，遍历表格每一行
                cells = row.find_all(['td', 'th'])

                if cells:                              # 跳过空单元格
                    """if len(cells) >= 3:  # 如果一行的单元格数大于或等于 3
                        country_name = cells[1].get_text(strip=True)  # 国家在第 2 列
                        visa_state = cells[2].get_text(strip=True)    # 免签信息在第 3 列"""
                    if len(cells) >= 2:  # 如果一行的单元格数为 2
                        country_name = cells[0].get_text(strip=True)  # 国家在第 1 列
                        visa_state = cells[1].get_text(strip=True)    # 免签信息在第 2 列
                    else:
                        continue  # 跳过其他不符合的行

                    country_name = re.sub(r'\[\d+\]', '', country_name).strip(); country_name = 'Eswatini' if country_name == 'Swaziland' else country_name     # 匹配掉方括号内容
                    visa_state = re.sub(r'\[\d+\]', '', visa_state).strip()
                    print(f"{country_name} | {visa_state}")   # 获取每一行country的visa policy       
                    
                    # 分类匹配
                    if "not required" in visa_state.lower() or "free" in visa_state.lower() or "unlimited" in visa_state.lower():
                        countries_visa_policy[0].append(country_name)
                    elif "arriv" in visa_state.lower() or "voa" in visa_state.lower():
                        countries_visa_policy[1].append(country_name)
                    elif "evisa" in visa_state.lower() or "eta" in visa_state.lower() or "electron" in visa_state.lower() or "online" in visa_state.lower(): 
                        countries_visa_policy[2].append(country_name)
                    elif "days" in visa_state.lower() or "week" in visa_state.lower() or "month" in visa_state.lower():
                        countries_visa_policy[0].append(country_name)

                    # 欧盟
                    if country_name == "European Union":
                        for i in european_union_countries:
                            countries_visa_policy[0].append(i)
                    
                    if country_name == "Schengen Area":
                        for i in schengen_area_countries:
                            countries_visa_policy[0].append(i)

        save_result_dict[country] = countries_visa_policy
        return countries_visa_policy

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {country}: {e}")
        return 0
 


def update_matrix(country, countries_visa_policy, G):
    # 遍历 countries_visa_policy 的每个列表 [[免签国家],[落地签国家],[电子签国家]]
    for policy_idx, nations_list in enumerate(countries_visa_policy):
        # 遍历每个国家名称
        for nation_with_policy in nations_list:
            # 检查国家是否在 DataFrame 的列中
            if nation_with_policy in G.columns:
                # 更新 DataFrame 中对应国家的互免签证关系
                G.loc[nation_with_policy, country] = policy_idx + 1  # 1: visa free, 2: visa on arrival, 3: eVisa
    #G.to_csv(f'visa_G_{date[:4]}.csv', index=True)
    return G


# 初始化免签网络矩阵
G = pd.DataFrame(0, index=nations_list, columns=nations_list)
index = 0 # 记录当前爬取的国家数量

def start(nations, G, index):
    # 爬取每个国家的免签数据并更新 DataFrame
    for country, citizen_name in list(nations.items())[index:]:
        print(f"Has already crawled {index} countries")
        print(f"Fetching data for {country}...")
        countries_visa_policy = fetch_visa_free_countries(country, citizen_name)    # 其它国家对country的免签政策, 爬取失败返回0
        
        # 如果爬取失败, countries_visa_policy == 0
        if countries_visa_policy == 0:
            # time.sleep(15)
            start(nations=nations, G=G, index=index)
            break

        G = update_matrix(country, countries_visa_policy, G)
        # 等待一会儿以避免过多请求
        time.sleep(random.uniform(1, 3))

        index += 1  # 爬取成功+1
        if index == len(nations):
            print(f"Successfully crawled {len(nations)} countries")
            # 保存 DataFrame 为 CSV 文件(在update_matrix这个函数中已保存)
            G.to_csv(f'visa_G_{str(date)[:4]}.csv', index=True)
            print(f"Visa matrix saved to visa_G_{str(date)[:4]}.csv")

start(nations=nations, G=G, index=index)