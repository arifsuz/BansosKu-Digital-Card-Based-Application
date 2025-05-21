import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from .db import get_connection


class BansosKuApp(toga.App):
    def startup(self):
        # Buat window utama
        self.main_window = toga.MainWindow(title=self.formal_name)

        # Tabel untuk menampilkan data warga
        self.warga_table = toga.Table(
            headings=["ID", "Nama", "NIK", "Alamat", "RT/RW", "Status"],
            accessors=["id", "nama", "nik", "alamat", "rt_rw", "status"],
            style=Pack(flex=1),
        )

        # Tombol untuk reload data
        reload_button = toga.Button(
            "Muat Ulang Data",
            on_press=self.load_data,
            style=Pack(padding=10)
        )

        # Tata letak (layout)
        box = toga.Box(
            children=[reload_button, self.warga_table],
            style=Pack(direction=COLUMN, padding=10)
        )

        # Set konten jendela
        self.main_window.content = box
        self.main_window.show()

        # Load data awal
        self.load_data()

    def load_data(self, widget=None):
        # Hapus data sebelumnya
        self.warga_table.data.clear()

        # Ambil data dari database
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nama, nik, alamat, rt_rw, status FROM warga")
        rows = cursor.fetchall()
        conn.close()

        # Tambahkan ke tabel
        for row in rows:
            self.warga_table.data.append({
                "id": str(row[0]),
                "nama": row[1],
                "nik": row[2],
                "alamat": row[3],
                "rt_rw": row[4],
                "status": row[5]
            })


def main():
    return BansosKuApp("BansosKu", "com.example.bansosku")
