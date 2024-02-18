# Shizuku
![Banner](.github/images/banner.png)
Shizuku adalah proyek pengambilan data yang menggunakan API SerpApi, sebuah platform yang menyediakan layanan API untuk melakukan pencarian seperti yang dapat dilakukan di Google dan layanan serupa. Dengan memanfaatkan SerpApi, Shizuku dirancang untuk mengakses dan mengumpulkan informasi secara efisien dari sumber data tersebut, membantu mempermudah proses pengambilan data untuk berbagai keperluan. Dengan dukungan API SerpApi, proyek ini memungkinkan akses yang handal dan terstruktur terhadap hasil pencarian, membuka peluang untuk analisis data yang mendalam dan penggunaan informasi yang lebih luas.

## Requirements
untuk menjalankan library ini,harus memiliki python dengan versi 3.10 hingga 3.12

## installasi
kamu bisa menginstall package `Shizuku` melalui via pip dengan cara

```sh
pip install git+https://github.com/kayabaakihiko13/Shizuku.git
```

## Example
```py
from Shizuku.call_api import ScrapingGoogleMap
api_key = "0aad998d63a0e029da9c884973946509231fb2209ee41f18cf1f6a9eadf3ec2d"
result = ScrapingGoogleMap(
    query="Mixue",api_key=api_key,lat=-7.275612, long=112.6302807, num_pages=5, results_per_page=20
)
```
dijalankan nanti muncul file bernama `maps-results.csv` setelah menjalankan kode tersebut.

untuk lebih lanjutnya bisa dibuka google collab seperti ini

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/16xOhPkdKMpohz3OiJpDY5qYLNrSzqn4H?usp=sharing)
