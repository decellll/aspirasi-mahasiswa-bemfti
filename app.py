from flask import Flask, render_template, request, flash, redirect, url_for
from database import create_aspiration

app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_in_production'  # Important for flash messages

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        kategori = request.form.get('kategori', 'lainnya')
        pesan = request.form.get('pesan', '').strip()

        if not pesan:
            flash('Pesan tidak boleh kosong!', 'error')
            return redirect(url_for('index'))

        try:
            create_aspiration(kategori, pesan)
            flash('Aspirasi berhasil dikirim!', 'success')
        except Exception as e:
            flash(f'Terjadi kesalahan: {str(e)}', 'error')

        return redirect(url_for('index'))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
