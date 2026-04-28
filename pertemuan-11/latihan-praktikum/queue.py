class Patient:
    def __init__(self, data):
        self.data = data
        self.next = None

class HospitalQueue:
    def __init__(self):
        self.head: Patient = None
        self.tail: Patient = None
        self.count = 0

    def is_empty(self):
        return self.head is None
    
    def enqueue(self, nama, keluhan):
        new_patient = Patient({
            "nama": nama,
            "keluhan": keluhan
        })

        if self.is_empty():
            self.head = self.tail = new_patient
        else:
            self.tail.next = new_patient
            self.tail = new_patient

        self.count += 1
        print(f"{nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self.count})")
    
    def dequeue(self):
        if self.is_empty():
            return
        
        patient_data = self.head.data
        self.head = self.head.next

        if self.is_empty():
            self.tail = None
        
        self.count -= 1
        return patient_data

    def peek(self):
        if self.is_empty():
            return
        return self.head.data
    
    def size(self):
        return self.count
    
    def clear(self):
        self.head = self.tail = None
        print("Sesi selesai. Antrian dikosongkan.")
    
    def print_queue(self):
        current = self.head
        count = 1

        while current:
            print(f"{count}. {current.data["nama"]} - {current.data["keluhan"]}")
            count += 1
            current = current.next



def main():
    antrian = HospitalQueue()
    is_empty = antrian.is_empty()
    print("Apakah antrian kosong?", "Ya" if is_empty else "Tidak")

    antrian.enqueue("Budi", "demam tinggi")
    antrian.enqueue("Ani", "batuk pilek")
    antrian.enqueue("Citra", "sakit kepala")
    print()

    print("Jumlah pasien menunggu:", antrian.size(), "orang")
    print()
    next_patient = antrian.peek()
    print(f"Pasien berikutnya: {next_patient["nama"]} - {next_patient["keluhan"]}")
    print()

    pasien = antrian.dequeue()
    print(f"Dokter memanggil: {pasien["nama"]} - {pasien["keluhan"]}")

    antrian.print_queue()
    print()

    antrian.enqueue("Dodi", "nyeri perut")
    print()

    pasien = antrian.dequeue()
    print(f"Dokter memanggil: {pasien["nama"]} - {pasien["keluhan"]}")

    print("Jumlah pasien menunggu:", antrian.size(), "orang")
    print()

    antrian.clear()
    is_empty = antrian.is_empty()
    print("Apakah antrian kosong?", "Ya" if is_empty else "Tidak")


if __name__ == "__main__":
    main()