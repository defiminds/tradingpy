bitcoin_balance = 10000.0
current_price = 30000.0
target_price = current_price * 0.9
num_entries = 6

btc_per_entry = []
usd_per_entry = []

for i in range(num_entries):
    # Calcula a quantidade de BTC necessária para alcançar o preço-alvo com base no número de entradas restantes
    btc_needed = (target_price * bitcoin_balance) / (current_price * (num_entries - i))

    # Adiciona o aumento necessário em BTC com base na quantidade necessária em vez do saldo restante
    if i == 0:
        increase_per_entry = btc_needed / bitcoin_balance
    else:
        increase_per_entry = (btc_needed - sum(btc_per_entry)) / (bitcoin_balance - sum(btc_per_entry))

    # Calcula a quantidade de BTC a ser comprada nesta entrada
    btc_per_entry.append(bitcoin_balance / (num_entries - i) * increase_per_entry)

    # Calcula o preço-alvo e o valor em dólares necessário para comprar a quantidade de BTC nesta entrada
    target_price_entry = current_price * (1 - (sum(btc_per_entry) / bitcoin_balance) * (num_entries - i) / (num_entries - i + 1))
    usd_per_entry.append(btc_per_entry[i] * target_price_entry)

    print(f"Entrada {i+1}: {btc_per_entry[i]:.8f} BTC")
    print(f"Preço em dólares: ${target_price_entry:,.2f}")
    print(f"Valor em dólares: ${usd_per_entry[i]:,.2f}\n")

total_usd = sum(usd_per_entry)
total_btc = sum(btc_per_entry)

print(f"Total de Bitcoins comprados: {total_btc:.8f} BTC")
print(f"Total em dólares gastos: ${total_usd:,.2f}")
