from django.shortcuts import render, redirect
from django.contrib import messages
from home.services import get_all_rows
from django.contrib.auth import logout
from django.shortcuts import redirect

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Ambil data dari Google Sheets
        users_data = get_all_rows("Test sheet", "login")
        

        # Cek apakah username dan password cocok
        for user in users_data:
           
            # Ubah password dari user menjadi string
            if user.get("username") == username and str(user.get("password")) == password:
                
                return redirect("/dashboard")

        # Jika tidak cocok, tampilkan pesan error
        messages.error(request, "Invalid username or password. Please try again.")
    
    return render(request, "login.html")





def user_logout(request):
    logout(request)  # Logout pengguna
    return redirect('login')  # Redirect ke halaman login setelah logout
