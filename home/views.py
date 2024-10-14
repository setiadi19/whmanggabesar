from django.shortcuts import render
from .services import get_all_rows  # Import fungsi dari services.py



def pivot(request):
    try:
        # Ambil data dari Sheet1
        data_sheet1 = get_all_rows("Test sheet", "Sheet1")
        # Ambil data dari Sheet 'intech'
        data_intech = get_all_rows("Test sheet", "intech")
        # Ambil data dari Sheet 'STOCK NTE'
        data_stock_nte = get_all_rows("Test sheet", "Pivot")
    except Exception as e:
        print(f"Error fetching Google Sheet data: {e}")
        data_sheet1 = []
        data_intech = []
        data_stock_nte = []

    # Proses data untuk STOCK NTE
    stock_nte_processed = []
    for row in data_stock_nte:
        stock_nte_processed.append({
            'NTE_EBIS': row.get('NTE EBIS', ''),
            'EBIS_NEW': row.get('EBIS NEW', ''),
            'EBIS_REFURBISH': row.get('EBIS REFURBISH', ''),
            'EBIS_DISMANTLING': row.get('EBIS DISMANTLING', ''),
            'NTE_TSEL': row.get('NTE TSEL', ''),
            'TSEL_NEW': row.get('TSEL NEW', ''),
            'TSEL_REFURBISH': row.get('TSEL REFURBISH', ''),
            'TSEL_DISMANTLING': row.get('TSEL DISMANTLING', ''),
            'NAMAA_TEKNISI': row.get('TEKNISI', ''),
            'PROVISIONING': row.get('PROVISIONING', ''),
            'ASSURANCE': row.get('ASSURANCE', ''),
        })

    # Proses data dari Sheet1
    stock_data = []
    for row in data_sheet1:
        stock_data.append({
            'description': row.get('Description', ''),
            'stock': row.get('Stock', 0)
        })

    # Proses data dari Sheet 'intech'
    intech_data = []
    for row in data_intech:
        intech_data.append({
            'TGL_PENGELUARAN': row.get('TGL PENGELUARAN', ''),
            'SN_BARU': row.get('SN BARU', ''),
            'SEGMENTASI_UNIT': row.get('SEGMENTASI UNIT', ''),
            'NIK_TEKNISI': row.get('NIK TEKNISI (SCMT)', ''),
            'NAMA_TEKNISI': row.get('NAMA TEKNISI', ''),
            'STATUS_NTE_BARU': row.get('STATUS NTE BARU', ''),
            'TELE_ID': row.get('TELE_ID', '')
        })
    
    # Kirim data ke template pivot.html
    context = {
        'stock_data': stock_data,
        'intech_data': intech_data,
        'data_stock_nte': stock_nte_processed,
    }

    return render(request, 'pivot.html', context)  # Render ke template pivot.html


# Create your views here.
def index(request):
    # Ambil data dari Google Sheets
    try:
        # # Ambil data dari Sheet1
        # data_sheet1 = get_all_rows("Test sheet", "Sheet1")
        # # Ambil data dari Sheet 'intech'
        # data_intech = get_all_rows("Test sheet", "intech")
        # # Ambil data dari Sheet 'STOCK NTE'
        data_stock_nte = get_all_rows("Test sheet", "Pivot")
    except Exception as e:
        print(f"Error fetching Google Sheet data: {e}")
        # data_sheet1 = []
        # data_intech = []
        data_stock_nte = []

    # Proses data untuk STOCK NTE
    stock_nte_processed = []
    for row in data_stock_nte:
        stock_nte_processed.append({
            # 'STATUS_EBIS': row.get('STATUS EBIS', ''),
            # 'TYPE_EBIS': row.get('TYPE EBIS', ''),
            # 'SN_EBIS': row.get('SN EBIS', ''),
            # 'KET_EBIS': row.get('KET EBIS', ''),
            # 'NTE_EBIS': row.get('NTE EBIS', ''),
            # 'EBIS_NEW': row.get('EBIS NEW', ''),
            # 'EBIS_REFURBISH': row.get('EBIS REFURBISH', ''),
            # 'EBIS_DISMANTLING': row.get('EBIS DISMANTLING', ''),

            # 'NTE_TSEL': row.get('NTE TSEL', ''),
            # 'TSEL_NEW': row.get('TSEL NEW', ''),
            # 'TSEL_REFURBISH': row.get('TSEL REFURBISH', ''),
            # 'TSEL_DISMANTLING': row.get('TSEL DISMANTLING', ''),

            'NAMAA_TEKNISI': row.get('TEKNISI', ''),
            'PROVISIONING': row.get('PROVISIONING', ''),
            'ASSURANCE': row.get('ASSURANCE', ''),
        })

    # # Proses data dari Sheet1
    # stock_data = []
    # for row in data_sheet1:
    #     stock_data.append({
    #         'description': row.get('Description', ''),  # Pastikan kolom 'Description' sesuai dengan Google Sheets
    #         'stock': row.get('Stock', 0)  # Pastikan kolom 'Stock' sesuai dengan Google Sheets
    #     })

    # # Proses data dari Sheet 'intech'
    # intech_data = []
    # for row in data_intech:
    #     intech_data.append({
    #         'TGL_PENGELUARAN': row.get('TGL PENGELUARAN', ''),
    #         'SN_BARU': row.get('SN BARU', ''),
    #         'SEGMENTASI_UNIT': row.get('SEGMENTASI UNIT', ''),
    #         'NIK_TEKNISI': row.get('NIK TEKNISI (SCMT)', ''),
    #         'NAMA_TEKNISI': row.get('NAMA TEKNISI', ''),
    #         'STATUS_NTE_BARU': row.get('STATUS NTE BARU', ''),
    #         'TELE_ID': row.get('TELE_ID', '')  # Ambil TELE_ID dengan aman
    #     })
        
    # Kirim data ke template
    context = {
        # 'stock_data': stock_data,
        # 'intech_data': intech_data,  # Kirim data dari sheet intech
        'data_stock_nte': stock_nte_processed,  # Kirim data stock NTE yang sudah diproses
    }

    return render(request, 'index.html', context)  # Pastikan Anda merender ke 'index.html'
