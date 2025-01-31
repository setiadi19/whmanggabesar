from django.shortcuts import render

from .services import get_all_rows

from django.http import JsonResponse, HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt




@csrf_exempt
def send_notification(request):
    if request.method == 'POST':
        tele_id = request.POST.get('tele_id')
        sn_baru = request.POST.get('sn_baru')
        segmentasi_unit = request.POST.get('segmentasi_unit')
        nama_teknisi = request.POST.get('nama_teknisi')

        # Memastikan bahwa tele_id tidak kosong
        if not tele_id:
            return JsonResponse({'status': 'error', 'message': 'TELE_ID tidak ditemukan atau kosong!'}, status=400)

        # Ganti TOKEN_BOT dengan token bot Telegram Anda
        bot_token = '6766498766:AAELsIzI1i4N5WRR96qnBzhyQHJ7Z5YQsJ4'
        
       # Buat pesan yang akan dikirim
        message = (
            f"🔔 *Notifikasi Baru!*\n\n"
            f"📌 *SN BARU:* {sn_baru}\n"
            f"🔍 *SEGMENTASI UNIT:* {segmentasi_unit}\n"
            f"👨‍🔧 *NAMA TEKNISI:* {nama_teknisi}\n\n"
            f"⚠️ Segera lakukan set install di aplikasi MYI.\n"
            f"Jika TIDAK bisa, segera hubungi Admin WH."
        )

        # URL API untuk mengirim pesan
        url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        

        payload = {
            'chat_id': tele_id,
            'text': message,
            'parse_mode': 'Markdown'  # Menentukan penggunaan Markdown untuk format
        }

        # Mengirim notifikasi
        response = requests.post(url, data=payload)

        # Memeriksa respon
        if response.status_code == 200:
            return HttpResponse(status=204)  # Tidak ada konten
        else:
            return JsonResponse({'status': 'error', 'message': f'Gagal mengirim notifikasi! Respon: {response.text}'}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request!'}, status=400)




def dashboard(request):
    try:
        # Ambil data dari Sheet 'intech'
        data = get_all_rows("Test sheet", "intech")  
    except Exception as e:
        print(f"Error fetching Google Sheet data: {e}")
        data = []

    # Filter hanya kolom yang diinginkan dan yang memiliki TELE_ID
    filtered_data = []
    for row in data:
        if row.get('TELE_ID'):  # Pastikan TELE_ID tidak kosong
            filtered_data.append({
                'TGL_PENGELUARAN': row.get('TGL', ''),
                'SN_BARU': row.get('SN', ''),  # Perbaiki agar sesuai dengan header di Google Sheets
                'SEGMENTASI_UNIT': row.get('UNIT', ''),
                'NIK_TEKNISI': row.get('NIK', ''),
                'NAMA_TEKNISI': row.get('NAMA', ''),
                'STATUS_NTE_BARU': row.get('STTUS', ''),
                'TELE_ID': row.get('TELE_ID', '')  
            })

    context = {
        'intech_data': filtered_data
    }
    
    return render(request, 'dashboard.html', context)
