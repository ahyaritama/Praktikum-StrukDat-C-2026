import tabulate

import konverter
import kurs

# Format mata uang
def curr_format(value):
    return f"{value:,.0f}".replace(",", ".")
 # Format mata uang rupiah
def idr_format(value):
    return f"Rp {curr_format(value)}"

# Input mata uang
def input_curr():
    curr_from = input("\nDari (IDR/USD/EUR/SGD/JPY): ").upper()
    curr_to = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()

    if (curr_from not in kurs.currency
            and curr_to not in kurs.currency):
        print("Masukkan mata uang yang benar!")
        return input_curr()

    return curr_from, curr_to

# Input jumlah mata uang
def input_value():
    try:
        value = float(input("Jumlah: "))
    except ValueError:
        print("Masukkan angka!\n")
        return input_value()

    return value

# Fungsi main
def main():
    try:
        print("=== KONVERTER MATA UANG ===")
        print(tabulate.tabulate(
            [[k, curr_format(v)] for k, v in kurs.currency.items()],
            headers=["Kode", " Kurs "],
            tablefmt="outline",
            disable_numparse=True,
            colalign=("left", "right")
        ))

        curr_from, curr_to = input_curr()
        value = input_value()
        result = konverter.convert(curr_from, curr_to, value)

        curr_from_text = idr_format(value) if curr_from == "IDR" else f"{value:,.2f} {curr_from}"
        curr_to_text = idr_format(result) if curr_to == "IDR" else f"{result:,.2f} {curr_to}"
        print(f"\n{curr_from_text} = {curr_to_text}")
    except KeyboardInterrupt:
        print()
        return

if __name__ == "__main__":
    main()