import webbrowser

def open_url(url):
    # เปิด URL ในเว็บเบราว์เซอร์
    webbrowser.open(url)

if __name__ == "__main__":
    # URL ที่ต้องการเปิด
    url = "https://www.facebook.com/AMshopcvc/"

    # เรียกใช้งานฟังก์ชันเพื่อเปิด URL
    open_url(url)
