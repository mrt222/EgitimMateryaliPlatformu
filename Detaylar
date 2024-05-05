sys: Bu modül, PyQt5 uygulamalarını başlatmak ve sonlandırmak için kullanılır. sys.argv komut satırı argümanlarını sağlar.
QApplication: PyQt5 uygulamalarının temelini oluşturan sınıftır. Uygulamayı başlatmak için kullanılır. exec_() metodu, uygulamanın çalışmasını sağlar.
QMainWindow: Ana pencere oluşturmak için kullanılır. Uygulamanın genel görünümü ve kullanıcı arayüzü elemanlarının yerleşimi burada yapılır.
QWidget: Kullanıcı arayüzünün temel yapı taşıdır. Diğer tüm widgetler bu sınıftan türetilir.
QVBoxLayout, QHBoxLayout: Dikey ve yatay sıralama için kullanılan yerleşim yöneticileridir. Widget'ları dikey veya yatay olarak düzenlemek için kullanılırlar.
QLabel: Metin veya görsel içerik görüntülemek için kullanılır.
QLineEdit: Tek satırlı metin girişi almak için kullanılır.
QPushButton: Tıklanabilir düğme oluşturmak için kullanılır.
QMessageBox: Kullanıcıya mesaj kutuları göstermek için kullanılır. Bilgi, uyarı veya hata mesajları göstermek için idealdir.
QInputDialog: Kullanıcıdan giriş almak için kullanılır. Metin, sayı veya liste gibi çeşitli giriş türlerini destekler.
QAction: Menü ve araç çubuklarındaki işlevsellik için kullanılır.
QMenu: Menü çubukları ve bağlam menüleri oluşturmak için kullanılır.
QFont: Yazı tipi ve boyutu gibi metin özelliklerini ayarlamak için kullanılır.
Qt: PyQt5'nin çeşitli özelliklerini içeren modüldür. Örneğin, Qt.AlignCenter gibi hizalama seçenekleri sağlar.
---------------------------------------------------
setGeometry(x, y, width, height): Bir pencerenin veya widget'ın konumunu ve boyutunu ayarlamak için kullanılır. x ve y, pencerenin ekran üzerindeki konumunu, width ve height ise boyutunu belirtir.
setWindowTitle(title): Pencerenin başlığını ayarlar.
setStyleSheet(styleSheet): Widget'ın stil sayfasını ayarlar. Stil sayfaları, widget'ların görünümünü CSS benzeri bir dil kullanarak özelleştirmek için kullanılır.
addLayout(layout): Bir layout'u mevcut bir layout içine ekler. Bu, iç içe geçmiş düzenler oluşturmak için kullanılır.
addWidget(widget): Bir widget'ı layout içine ekler.
clicked.connect(slot_function): Butona tıklandığında çalışacak bir işlev (slot) bağlamak için kullanılır. Örneğin, butona tıklandığında bir fonksiyon çağırmak için kullanılır.
setFont(font): Bir widget için yazı tipi özelliklerini ayarlar.
show(): Widget'ı ekranda göstermek için kullanılır.
hide(): Widget'ı ekranda gizlemek için kullanılır.
close(): Widget'ı kapatmak için kullanılır.
font(): Bir widget için varsayılan yazı tipi özelliklerini döndürür.
setCentralWidget(widget): Ana pencerenin merkezine bir widget yerleştirir. Bu genellikle bir QMainWindow kullanılırken ana içeriği göstermek için kullanılır.
menuBar(): Bir ana pencereye menü çubuğu ekler.
addAction(action): Bir QAction'ı bir menüye veya araç çubuğuna ekler.
triggered.connect(slot_function): Bir QAction tetiklendiğinde çalışacak bir işlev (slot) bağlamak için kullanılır.
setText(text): Bir QLabel'ın metnini ayarlar.
setAlignment(alignment): Bir QLabel'ın metin hizalamasını ayarlar.
get_text(): Kullanıcıdan metin girmesini sağlar ve girdiyi döndürür.
information(parent, title, message): Bilgi mesaj kutusu gösterir.
warning(parent, title, message): Uyarı mesaj kutusu gösterir.
setEchoMode(mode): Bir QLineEdit'in metin giriş modunu ayarlar. Örneğin, QLineEdit.Password ile şifre girme modunu açar.
------------------------------------------------------------------------------------------------------------------------
Kullanıcı adı ve şifreyi girdikten sonra "Giriş Yap" düğmesine basılırsa, doğru bilgilerle ana pencereye yönlendirilir. Aksi takdirde, hatalı giriş uyarısı alır. 
Bu kontrol check_credentials() fonksiyonunda gerçekleşir.Ana pencere, kullanıcıyı eğitim derslerinin bulunduğu bir ortama yönlendirir. Ana pencerenin üst kısmında, 
kullanıcıya hoş geldiniz mesajı ve o dönem alınan derslerin listesi görüntülenir. Ayrıca, çıkış yapmak için bir düğme bulunur.
Ana pencerenin alt kısmında, her bir ders için ayrılan kutucuklar yer alır. Bu kutucuklar, ders adı, öğretmen ve ders içeriği bilgilerini içerir. Her dersin yanında, 
"İzlemeye Başla", "Ödev Yükle" ve "Öğretmene Soru Sor" düğmeleri bulunur. Bu düğmeler, dersle ilgili işlemleri gerçekleştirmek için kullanılır.
Kullanıcı "İzlemeye Başla" düğmesine tıklarsa, ilgili dersi izlemeye başladığına dair bir uyarı alır. Eğer ders zaten izleniyorsa, uyarı alır. "Ödev Yükle" düğmesine
tıklarsa, ilgili ders için ödev yüklendiğine dair bir uyarı alır. "Öğretmene Soru Sor" düğmesine tıklarsa, öğretmene bir soru gönderir.
Ayrıca, menü çubuğuyla kullanıcının profil bilgilerine ve izlediği derslere erişim sağlanır. "Kullanıcı Bilgileri" seçeneği, kullanıcının kişisel bilgilerini gösterirken, 
"İzlediğim Dersler" seçeneği, kullanıcının o dönem izlediği dersleri listeler.
