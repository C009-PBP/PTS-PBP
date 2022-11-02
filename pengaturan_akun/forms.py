from django import forms
from django.contrib.auth.models import User
from pengaturan_akun.models import Profile

GENDER = ( 
('Laki-Laki','Laki-Laki'),
('Perempuan','Perempuan')
)

PROVINCES = (
    ('Aceh', 'Aceh'),
    ('Sumatra Utara', 'Sumatra Utara'),
    ('Sumatra Barat', 'Sumatra Barat'),
    ('Riau', 'Riau'),
    ('Kep. Riau', 'Kep. Riau'),
    ('Jambi', 'Jambi'),
    ('Bengkulu', 'Bengkulu'),
    ('Sumatra Selatan', 'Sumatra Selatan'),
    ('Kep. Bangka Belitung', 'Kep. Bangka Belitung'),
    ('Lampung', 'Lampung'),
    ('Banten', 'Banten'),
    ('DKI Jakarta', 'DKI Jakarta'),
    ('Jawa Barat', 'Jawa Barat'),
    ('Jawa Tengah', 'Jawa Tengah'),
    ('DI Yogyakarta', 'DI Yogyakarta'),
    ('Jawa Timur', 'Jawa Timur'),
    ('Bali', 'Bali'),
    ('NTB', 'NTB'),
    ('NTT', 'NTT'),
    ('Kalimantan Barat', 'Kalimantan Barat'),
    ('Kalimantan Tengah', 'Kalimantan Tengah'),
    ('Kalimantan Selatan', 'Kalimantan Selatan'),
    ('Kalimantan Timur', 'Kalimantan Timur'),
    ('Kalimantan Utara', 'Kalimantan Utara'),
    ('Sulawesi Barat', 'Sulawesi Barat'),
    ('Sulawesi Selatan', 'Sulawesi Selatan'),
    ('Sulawesi Tenggara', 'Sulawesi Tenggara'),
    ('Sulawesi Tengah', 'Sulawesi Tengah'),
    ('Gorontalo', 'Gorontalo'),
    ('Sulawesi Utara', 'Sulawesi Utara'),
    ('Maluku Utara', 'Maluku Utara'),
    ('Maluku', 'Maluku'),
    ('Papua Barat', 'Papua Barat'),
    ('Papua', 'Papua'),
    ('Papua Tengah', 'Papua Tengah'),
    ('Papua Pegunungan', 'Papua Pegunungan'),
    ('Papua Selatan', 'Papua Selatan'),
)

GOLDAR = ( 
('A','A'),
('B','B'),
('AB','AB'),
('O','O'),
)

class EditProfile(forms.ModelForm):
    first_name = forms.CharField(label='Nama Depan:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Depan', 'name': 'first_name'}))
    last_name = forms.CharField(label='Nama Belakang:', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nama Belakang', 'name': 'last_name'}))
    phone_no = forms.CharField(label='No. Telepon:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'No. Telepon', 'name': 'phone_no'}))
    email= forms.EmailField(label='Email:', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'name': 'email'}))
    birth_date = forms.DateField(label='Tanggal Lahir:', widget=forms.DateInput(attrs= {'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'name': 'birth_date'}))
    street = forms.CharField(label='Alamat:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alamat', 'name': 'street'}))
    city = forms.CharField(label='Kota:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kota', 'name': 'city'}))
    province = forms.CharField(label='Provinsi:', widget=forms.Select(choices=PROVINCES, attrs={'class': 'form-select', 'name': 'province'}))
    gender = forms.ChoiceField(label='Jenis Kelamin:', choices=GENDER, widget=forms.RadioSelect(attrs={'name': 'gender'}))
    profile_pic = forms.ImageField(label='Foto Profil:', widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'name': 'profile_pic'}))
   
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone_no', 'email', 'birth_date', 'street', 'city', 'province', 'gender', 'profile_pic']

class EditEmergencyContact(forms.ModelForm):
    emergency_firstname = forms.CharField(label='Nama Depan:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Depan', 'name': 'emergency_firstname'}))
    emergency_lastname = forms.CharField(label='Nama Belakang:', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nama Belakang', 'name': 'emergency_lastname'}))
    emergency_relationship = forms.CharField(label='Hubungan Dengan Pasien:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hubungan dengan pasien', 'name': 'emergency_relationship'}))
    emergency_phone_no = forms.CharField(label='No. Telepon:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'No. Telepon', 'name': 'emergency_phone_no'}))
    emergency_street = forms.CharField(label='Alamat:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alamat', 'name': 'emergency_street'}))
    emergency_city = forms.CharField(label='Kota:',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kota', 'name': 'emergency_city'}))
    emergency_province = forms.CharField(label='Provinsi:', widget=forms.Select(choices=PROVINCES, attrs={'class': 'form-select', 'name': 'emergency_province'}))

    class Meta:
        model = Profile
        fields = ['emergency_firstname', 'emergency_lastname', 'emergency_relationship', 'emergency_phone_no', 'emergency_street', 'emergency_city', 'emergency_province']

class EditMedRecord(forms.ModelForm):
    bloodtype = forms.CharField(label='Golongan Darah:', widget=forms.Select(choices=GOLDAR, attrs={'class': 'form-select', 'name': 'bloodtype'}))
    bloodpressure = forms.CharField(label='Tekanan Darah:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tekanan Darah (mmHg)'}))
    illnesses = forms.CharField(label='Riwayat Penyakit:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Riwayat Alergi'}))
    allergies = forms.CharField(label='Riwayat Alergi:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Riwayat Alergi'}))

    class Meta:
        model = Profile
        fields = ['bloodtype', 'bloodpressure', 'illnesses', 'allergies']