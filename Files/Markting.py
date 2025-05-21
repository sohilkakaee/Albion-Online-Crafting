#<<<___Script BY Sohilkakaee___>>>

import requests
import time
from difflib import get_close_matches

# === Tanzimat ===
SHAHR_HA = [
    "Martlock", "Lymhurst", "Bridgewatch", "Fort Sterling", "Thetford", "Caerleon", "Brecilien"
]
MAVAD_MOTABAR = ["CLOTH", "LEATHER", "METALBAR", "PLANKS", "WOOD", "ORE", "FIBER", "HIDE"]
OTHER_MAVAD = ["ARCANE_ESSENCE", "HERB", "MUSHROOM", "ESSENCE"]  # Baraye potion

# Peyghamha baraye zabanhaye mokhtalef
MESSAGES = {
    "finglish": {
        "choose_lang": "Zaban barname ra entekhab kon (finglish ya english): ",
        "invalid_lang": "Zaban motabar nist. Lotfan 'finglish' ya 'english' vared kon.",
        "item_type_prompt": "Aya mikhay Potion besazi ya Other Item? ([BETA]potion/other): ",
        "invalid_item_type": "Gozine motabar nist. Lotfan 'potion' ya 'other' vared kon.",
        "item_name_prompt": "Esm item ra vared kon (mesal: T6_POTION_HEAL , ya khali baraye skip): ",
        "item_price_display": "\n📊 Gheymat foroosh {item_id} (ba tavajoh be Quality):",
        "quality_price": "  • Quality {quality}: {price} Silver (shahr: {city})",
        "no_item_price": "⚠️ Gheymati baraye {item_id} peyda nashod. Lotfan esm dorost vared kon ya gheymat foroosh dasti vared kon.",
        "server_prompt": "Kodoom server? (west, east, europe): ",
        "invalid_option": "Meghdar motabar nist. Gozinehaye motabar: {options}",
        "tier_prompt": "Tier item (T4, T5, T6, T7, T8): ",
        "enchant_prompt": "Enchantment (khali='', .1, .2, .3 .4): ",
        "input_error": "❌ Khata dar vorodi: {error}. Lotfan dobare vared kon.",
        "keyboard_interrupt": "❌ Barname tavasot karbar motavaqf shod.",
        "number_prompt": "Lotfan adad vared kon.",
        "non_negative_prompt": "Lotfan meghdar gheyr-manfi vared kon.",
        "number_error": "❌ Khata dar adad: {error}. Lotfan dobare vared kon.",
        "material_prompt": "Esm mavade avalie ra vared kon (mesal: CLOTH, LEATHER, METALBAR, PLANKS,WOOD, ORE, FIBER, HIDE, ya har esm digar): ",
        "material_amount": "Che tedad {material} baraye 1 item lazem ast? ",
        "more_materials": "Mavade avalie digari dari? (y/n): ",
        "material_error": "❌ Khata dar vorodi mavad: {error}",
        "similar_materials": "Mavad moghabel baraye {material}: {similar}. Aya mikhay yeki az inha ra entekhab koni? (y/n): ",
        "choose_similar": "Kodoom mavade moghabel ra mikhay? (esm ra vared kon): ",
        "api_url": "🔗 URL darkhast API: {url}",
        "api_error": "❌ Khata dar API: Code vaziyat {status}",
        "api_invalid_data": "❌ Data az API format motabar nadarad.",
        "api_invalid_entry": "⚠️ Data gheyr motabar az API: {entry}",
        "api_connection_error": "❌ Khata dar ertebat ba API: {error}",
        "api_response_error": "❌ Khata dar pasokh API: {error}",
        "no_price_found": "⚠️ Hich gheymati baraye {item_id} peyda nashod. Lotfan sure konid item dar bazar mojood ast ya esm dorost ast.",
        "price_display": "\n📊 Gheymat {item_id}:",
        "city_price": "  • {city}: {price} Silver",
        "cheapest_city": "🟢 Arzoon-tarin shahr: {city} - {price} Silver",
        "most_expensive_city": "🔴 Geran-tarin shahr: {city} - {price} Silver",
        "no_prices": "❌ Natonestim gheymat mavad avalie ra daryaft konim. Lotfan server ya internet ra check kon.",
        "no_valid_prices": "❌ Hich mavade avalie gheymat motabar nadasht. Barname motavaqf mishavad.",
        "material_price_error": "❌ Gheymat baraye {material} peyda nashod. Az in mavade gozashtim.",
        "material_price_fetch_error": "❌ Khata dar pasokh gheymat mavad: {error}",
        "other_costs_prompt": "\n💰 Hazinehaye janebi (mesalan ghaza, maliat): ",
        "sell_price_prompt": "💸 Gheymat foroosh har item: ",
        "quantity_prompt": "🔢 Chand ta mikhay besazi? ",
        "cost_error": "❌ Khata dar hazineha ya tedad: {error}",
        "material_cost_details": "\n📋 Juziyyat hazine mavad:",
        "material_cost": "  • {material}: {amount} * {price} = {total} Silver",
        "result_title": "\n🎯 Natije:",
        "material_cost_total": "✅ Hazine mavad avalie har item: {cost:.2f} Silver",
        "total_cost": "✅ Hazine kolli (ba janebi): {cost:.2f} Silver",
        "profit_no_focus": "💰 Sood har item bedoone Focus: {profit:.2f} Silver",
        "profit_with_focus": "💰 Sood har item ba Focus (35% return): {profit:.2f} Silver",
        "total_profit": "\n📦 Sood baraye {quantity} item:",
        "total_profit_no_focus": "▪️ Bedoone Focus: {profit:.2f} Silver",
        "total_profit_with_focus": "▪️ Ba Focus: {profit:.2f} Silver",
        "negative_profit_warning": "\n⚠️ Hoshdar: Sood manfi shode! Lotfan gheymat foroosh, tedad mavad, ya hazine janebi ra check kon.",
        "calculation_error": "❌ Khata dar mohasebat: {error}",
        "run_again_prompt": "\n🔁 Aya mikhay dobare ejra koni? (y/n): ",
        "exit_message": "📤 Barname khateme yaft. Movafagh bashi!",
        "main_error": "❌ Khata: {error}. Lotfan dobare talash kon."
    },
    "english": {
        "choose_lang": "Choose program language (finglish or english): ",
        "invalid_lang": "Invalid language. Please enter 'finglish' or 'english'.",
        "item_type_prompt": "Do you want to craft a Potion or Other Item? ([BETA]potion/other): ",
        "invalid_item_type": "Invalid option. Please enter 'potion' or 'other'.",
        "item_name_prompt": "Enter item name (e.g., T6_POTION_HEAL , or leave empty to skip): ",
        "item_price_display": "\n📊 Sell price for {item_id} (by Quality):",
        "quality_price": "  • Quality {quality}: {price} Silver (city: {city})",
        "no_item_price": "⚠️ No price found for {item_id}. Please enter correct name or input sell price manually.",
        "server_prompt": "Which server? (west, east, europe): ",
        "invalid_option": "Invalid input. Valid options: {options}",
        "tier_prompt": "Item tier (T4, T5, T6, T7, T8): ",
        "enchant_prompt": "Enchantment (empty='', .1, .2, .3 .4): ",
        "input_error": "❌ Input error: {error}. Please try again.",
        "keyboard_interrupt": "❌ Program stopped by user.",
        "number_prompt": "Please enter a number.",
        "non_negative_prompt": "Please enter a non-negative number.",
        "number_error": "❌ Number error: {error}. Please try again.",
        "material_prompt": "Enter material name (e.g., CLOTH, LEATHER, METALBAR, PLANKS,WOOD, ORE, FIBER, HIDE, or any other): ",
        "material_amount": "How many {material} are needed for 1 item? ",
        "more_materials": "Any more materials? (y/n): ",
        "material_error": "❌ Material input error: {error}",
        "similar_materials": "Similar materials for {material}: {similar}. Would you like to choose one of these? (y/n): ",
        "choose_similar": "Which similar material would you like? (enter name): ",
        "api_url": "🔗 API request URL: {url}",
        "api_error": "❌ API error: Status code {status}",
        "api_invalid_data": "❌ API data has invalid format.",
        "api_invalid_entry": "⚠️ Invalid API data: {entry}",
        "api_connection_error": "❌ API connection error: {error}",
        "api_response_error": "❌ API response error: {error}",
        "no_price_found": "⚠️ No price found for {item_id}. Please ensure the item exists in the market or the name is correct.",
        "price_display": "\n📊 Price for {item_id}:",
        "city_price": "  • {city}: {price} Silver",
        "cheapest_city": "🟢 Cheapest city: {city} - {price} Silver",
        "most_expensive_city": "🔴 Most expensive city: {city} - {price} Silver",
        "no_prices": "❌ Could not fetch material prices. Please check server or internet connection.",
        "no_valid_prices": "❌ No materials have valid prices. Program will stop.",
        "material_price_error": "❌ No price found for {material}. Skipping this material.",
        "material_price_fetch_error": "❌ Error fetching material prices: {error}",
        "other_costs_prompt": "\n💰 Other costs (e.g., food, taxes): ",
        "sell_price_prompt": "💸 Sell price per item: ",
        "quantity_prompt": "🔢 How many items to craft? ",
        "cost_error": "❌ Error in costs or quantity: {error}",
        "material_cost_details": "\n📋 Material cost details:",
        "material_cost": "  • {material}: {amount} * {price} = {total} Silver",
        "result_title": "\n🎯 Result:",
        "material_cost_total": "✅ Material cost per item: {cost:.2f} Silver",
        "total_cost": "✅ Total cost (with other costs): {cost:.2f} Silver",
        "profit_no_focus": "💰 Profit per item without Focus: {profit:.2f} Silver",
        "profit_with_focus": "💰 Profit per item with Focus (35% return): {profit:.2f} Silver",
        "total_profit": "\n📦 Profit for {quantity} items:",
        "total_profit_no_focus": "▪️ Without Focus: {profit:.2f} Silver",
        "total_profit_with_focus": "▪️ With Focus: {profit:.2f} Silver",
        "negative_profit_warning": "\n⚠️ Warning: Negative profit! Please check sell price, material amounts, or other costs.",
        "calculation_error": "❌ Calculation error: {error}",
        "run_again_prompt": "\n🔁 Do you want to run again? (y/n): ",
        "exit_message": "📤 Program ended. Good luck!",
        "main_error": "❌ Error: {error}. Please try again."
    }
}

QUALITY_MAP = {
    1: "Normal",
    2: "Good",
    3: "Outstanding",
    4: "Excellent",
    5: "Masterpiece"
}

def begir_vorodi(prompt, gozineha=None, lang="finglish", **kwargs):
    while True:
        try:
            meghdar = input(MESSAGES[lang][prompt].format(**kwargs)).strip()
            if gozineha:
                if meghdar.lower() not in [opt.lower() for opt in gozineha]:
                    print(MESSAGES[lang]["invalid_option"].format(options=gozineha))
                    continue
            return meghdar
        except KeyboardInterrupt:
            print(MESSAGES[lang]["keyboard_interrupt"])
            exit()
        except Exception as e:
            print(MESSAGES[lang]["input_error"].format(error=e))
            continue

def begir_adad_float(prompt, lang="finglish", **kwargs):
    while True:
        try:
            meghdar = float(input(MESSAGES[lang][prompt].format(**kwargs)).strip())
            if meghdar < 0:
                print(MESSAGES[lang]["non_negative_prompt"])
            else:
                return meghdar
        except ValueError:
            print(MESSAGES[lang]["number_prompt"])
        except KeyboardInterrupt:
            print(MESSAGES[lang]["keyboard_interrupt"])
            exit()
        except Exception as e:
            print(MESSAGES[lang]["number_error"].format(error=e))
            continue

def begir_gheymatha(item_ids, server, lang="finglish"):
    url = f"https://{server}.albion-online-data.com/api/v2/stats/prices/{','.join(item_ids)}?locations={','.join(SHAHR_HA)}"
    print(MESSAGES[lang]["api_url"].format(url=url))
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(MESSAGES[lang]["api_error"].format(status=response.status_code))
            return None

        data = response.json()
        if not isinstance(data, list):
            print(MESSAGES[lang]["api_invalid_data"])
            return None

        gheymatha = {item_id: {} for item_id in item_ids}
        for entry in data:
            if not isinstance(entry, dict) or 'city' not in entry or 'item_id' not in entry:
                print(MESSAGES[lang]["api_invalid_entry"].format(entry=entry))
                continue
            shahr = entry['city']
            item_id = entry['item_id']
            gheymat = entry.get("sell_price_min", 0)
            quality = entry.get("quality", 1)
            if gheymat > 0:
                gheymatha[item_id].setdefault(quality, {})[shahr] = gheymat

        return gheymatha

    except requests.exceptions.RequestException as e:
        print(MESSAGES[lang]["api_connection_error"].format(error=e))
        return None
    except Exception as e:
        print(MESSAGES[lang]["api_response_error"].format(error=e))
        return None

def neshon_bede_gheymatha(item_id, gheymatha, lang="finglish", is_item=False):
    if not gheymatha or not any(gheymatha.values()):
        all_materials = MAVAD_MOTABAR + OTHER_MAVAD
        material_name = item_id.split('_')[-1].split('@')[0]
        similar = get_close_matches(material_name, all_materials, n=3, cutoff=0.6)
        if similar and not is_item:
            print(MESSAGES[lang]["similar_materials"].format(material=material_name, similar=', '.join(similar)))
            if begir_vorodi("similar_materials", ['y', 'n'], lang, material=material_name, similar=', '.join(similar)) == 'y':
                new_material = begir_vorodi("choose_similar", lang=lang)
                return new_material
        print(MESSAGES[lang]["no_price_found"].format(item_id=item_id))
        return None

    if is_item:
        print(MESSAGES[lang]["item_price_display"].format(item_id=item_id))
        for quality, cities in gheymatha.items():
            if cities:
                cheapest_city = min(cities, key=cities.get)
                print(MESSAGES[lang]["quality_price"].format(
                    quality=QUALITY_MAP.get(quality, quality),
                    price=cities[cheapest_city],
                    city=cheapest_city
                ))
        return None  # Baraye item, gheymat barmigardoonim ta dasti vared she
    else:
        shahr_bala = max(gheymatha[1], key=gheymatha[1].get) if 1 in gheymatha else list(gheymatha.keys())[0]
        shahr_paeen = min(gheymatha[1], key=gheymatha[1].get) if 1 in gheymatha else list(gheymatha.keys())[0]

        print(MESSAGES[lang]["price_display"].format(item_id=item_id))
        for shahr, gheymat in gheymatha.get(1, {}).items():
            print(MESSAGES[lang]["city_price"].format(city=shahr, price=gheymat))
        print(MESSAGES[lang]["cheapest_city"].format(city=shahr_paeen, price=gheymatha[1][shahr_paeen]))
        print(MESSAGES[lang]["most_expensive_city"].format(city=shahr_bala, price=gheymatha[1][shahr_bala]) + "\n")

        return gheymatha[1][shahr_paeen] if 1 in gheymatha else list(gheymatha.values())[0][shahr_paeen]

def ejra(lang="finglish"):
    # 🌍 Entekhab Server
    try:
        server = begir_vorodi("server_prompt", ['west', 'east', 'europe'], lang)
    except Exception as e:
        print(MESSAGES[lang]["input_error"].format(error=e))
        return

    # Entekhab noo item
    try:
        item_type = begir_vorodi("item_type_prompt", ['potion', 'other'], lang)
    except Exception as e:
        print(MESSAGES[lang]["input_error"].format(error=e))
        return

    # Tier va Enchantment
    try:
        tier = begir_vorodi("tier_prompt", ['T4', 'T5', 'T6', 'T7', 'T8'], lang)
        enchant_level = ''
        if item_type.lower() == 'other':
            enchant = begir_vorodi("enchant_prompt", ['', '.1', '.2', '.3','.4'], lang)
            enchant_level = enchant.replace('.', '') if enchant else ''
    except Exception as e:
        print(MESSAGES[lang]["input_error"].format(error=e))
        return

    # Esm item va gheymat foroosh
    try:
        item_name = begir_vorodi("item_name_prompt", lang=lang)
        if item_name:
            item_id = item_name if item_name.startswith('T') else f"{tier}_{item_name}"
            if item_type.lower() == 'other' and enchant_level:
                item_id += f"_LEVEL{enchant_level}@{enchant_level}"
            gheymatha_data = begir_gheymatha([item_id], server, lang)
            if gheymatha_data and gheymatha_data.get(item_id):
                neshon_bede_gheymatha(item_id, gheymatha_data[item_id], lang, is_item=True)
            else:
                print(MESSAGES[lang]["no_item_price"].format(item_id=item_id))
    except Exception as e:
        print(MESSAGES[lang]["input_error"].format(error=e))

    # === Mavad Avaliye ===
    print("\n" + MESSAGES[lang]["material_prompt"].format(materials=', '.join(MAVAD_MOTABAR + OTHER_MAVAD)))
    mavad = {}
    item_ids = []
    try:
        while True:
            esm_mavad = begir_vorodi("material_prompt", lang=lang, materials=', '.join(MAVAD_MOTABAR + OTHER_MAVAD))
            mat_id = f"{tier}_{esm_mavad}"
            if item_type.lower() == 'other' and enchant_level:
                mat_id += f"_LEVEL{enchant_level}@{enchant_level}"
            item_ids.append(mat_id)

            tedad_mavad = begir_adad_float("material_amount", lang, material=esm_mavad)
            mavad[esm_mavad] = {"id": mat_id, "tedad": tedad_mavad}

            edame = begir_vorodi("more_materials", ['y', 'n'], lang)
            if edame.lower() == 'n':
                break
    except Exception as e:
        print(MESSAGES[lang]["material_error"].format(error=e))
        return

    # Daryaft gheymatha
    time.sleep(0.5)  # Takhir koochak baraye API
    gheymatha_data = begir_gheymatha(item_ids, server, lang)
    if not gheymatha_data:
        print(MESSAGES[lang]["no_prices"])
        return

    try:
        for esm_mavad, info in mavad.items():
            mat_id = info["id"]
            gheymatha = gheymatha_data.get(mat_id, {})
            result = neshon_bede_gheymatha(mat_id, gheymatha, lang)
            if result is None:
                print(MESSAGES[lang]["material_price_error"].format(material=esm_mavad))
                continue
            if isinstance(result, str):
                new_mat_id = f"{tier}_{result}"
                if item_type.lower() == 'other' and enchant_level:
                    new_mat_id += f"_LEVEL{enchant_level}@{enchant_level}"
                item_ids[item_ids.index(mat_id)] = new_mat_id
                mavad[esm_mavad]["id"] = new_mat_id
                gheymatha_data = begir_gheymatha([new_mat_id], server, lang)
                if not gheymatha_data:
                    print(MESSAGES[lang]["material_price_error"].format(material=result))
                    continue
                gheymatha = gheymatha_data.get(new_mat_id, {})
                gheymat_mavad = neshon_bede_gheymatha(new_mat_id, gheymatha, lang)
                if gheymat_mavad is None:
                    print(MESSAGES[lang]["material_price_error"].format(material=result))
                    continue
                mavad[esm_mavad]["gheymat"] = gheymat_mavad
            else:
                mavad[esm_mavad]["gheymat"] = result
    except Exception as e:
        print(MESSAGES[lang]["material_price_fetch_error"].format(error=e))
        return

    if not any("gheymat" in info for info in mavad.values()):
        print(MESSAGES[lang]["no_valid_prices"])
        return

    # === Hazineha ===
    try:
        hazine_janebi = begir_adad_float("other_costs_prompt", lang)
        gheymat_foroosh = begir_adad_float("sell_price_prompt", lang)
        tedad = begir_adad_float("quantity_prompt", lang)
    except Exception as e:
        print(MESSAGES[lang]["cost_error"].format(error=e))
        return

    # === Mohasebe ===
    try:
        majmoo_hazine_mavad = sum(info["gheymat"] * info["tedad"] for info in mavad.values() if "gheymat" in info)
        print(MESSAGES[lang]["material_cost_details"])
        for esm_mavad, info in mavad.items():
            if "gheymat" in info:
                print(MESSAGES[lang]["material_cost"].format(
                    material=esm_mavad, amount=info["tedad"], price=info["gheymat"], total=info["tedad"] * info["gheymat"]
                ))

        hazine_kolli_baraye_har_item = majmoo_hazine_mavad + hazine_janebi
        sood_bedoone_focus = gheymat_foroosh - hazine_kolli_baraye_har_item

        # Focus return 35%
        hazine_mavad_ba_focus = sum((info["gheymat"] * info["tedad"]) * (1 - 0.35) for info in mavad.values() if "gheymat" in info)
        sood_ba_focus = gheymat_foroosh - (hazine_mavad_ba_focus + hazine_janebi)

        majmoo_sood_bedoone_focus = sood_bedoone_focus * tedad
        majmoo_sood_ba_focus = sood_ba_focus * tedad

        # === Natije ===
        print(MESSAGES[lang]["result_title"])
        print(MESSAGES[lang]["material_cost_total"].format(cost=majmoo_hazine_mavad))
        print(MESSAGES[lang]["total_cost"].format(cost=hazine_kolli_baraye_har_item))
        print(MESSAGES[lang]["profit_no_focus"].format(profit=sood_bedoone_focus))
        print(MESSAGES[lang]["profit_with_focus"].format(profit=sood_ba_focus))
        print(MESSAGES[lang]["total_profit"].format(quantity=int(tedad)))
        print(MESSAGES[lang]["total_profit_no_focus"].format(profit=majmoo_sood_bedoone_focus))
        print(MESSAGES[lang]["total_profit_with_focus"].format(profit=majmoo_sood_ba_focus))

        if sood_bedoone_focus < 0 or sood_ba_focus < 0:
            print(MESSAGES[lang]["negative_profit_warning"])

    except Exception as e:
        print(MESSAGES[lang]["calculation_error"].format(error=e))
        return

def asli():
    lang = begir_vorodi("choose_lang", ['finglish', 'english'], lang="finglish")
    if lang.lower() not in ['finglish', 'english']:
        print(MESSAGES["finglish"]["invalid_lang"])
        return

    while True:
        try:
            ejra(lang)
            dobare = begir_vorodi("run_again_prompt", ['y', 'n'], lang)
            if dobare.lower() == 'n':
                print(MESSAGES[lang]["exit_message"])
                break
        except Exception as e:
            print(MESSAGES[lang]["main_error"].format(error=e))
            break

if __name__ == "__main__":
    asli()