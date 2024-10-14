from django.shortcuts import render
from .services import get_all_rows  # Pastikan Anda mengimpor fungsi ini

def dashboard(request):
    try:
        # Ambil data dari Sheet 'intech'
        data = get_all_rows("Test sheet", "intech")  # Sesuaikan dengan nama sheet yang diinginkan
    except Exception as e:
        # Tangani kesalahan jika ada
        print(f"Error fetching Google Sheet data: {e}")
        data = []

    # Filter hanya kolom yang diinginkan
    filtered_data = []
    for row in data:
        filtered_data.append({
            'TGL_PENGELUARAN': row.get('TGL PENGELUARAN', ''),
            'SN_BARU': row.get('SN BARU', ''),
            'SEGMENTASI_UNIT': row.get('SEGMENTASI UNIT', ''),
            'NIK_TEKNISI': row.get('NIK TEKNISI (SCMT)', ''),
            'NAMA_TEKNISI': row.get('NAMA TEKNISI', ''),
            'STATUS_NTE_BARU': row.get('STATUS NTE BARU', ''),
            'TELE_ID': row.get('TELE_ID', '')  # Ambil TELE_ID dengan aman
        })

    # Kirim data ke template
    context = {
        'intech_data': filtered_data
    }
    
    return render(request, 'dashboard.html', context)  # Pastikan template ini ada
