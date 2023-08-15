import tkinter as tk
import random


class VocabularyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kelime Öğrenme Uygulaması")

        self.words = []
        self.index = 0

        self.english_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.english_label.pack(pady=20)

        self.show_button = tk.Button(root, text="Göster", command=self.show_translation)
        self.show_button.pack(pady=10)

        self.next_button = tk.Button(root, text="Sonraki", command=self.show_next_word)
        self.next_button.pack(pady=10)

        self.translation_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.translation_label.pack(pady=20)

        self.load_words()
        self.show_word()

    def load_words(self):
        self.words = [("A (Determiner): I have a book on my desk.", "A (Belirleyici): Masamın üzerinde bir kitap var."),
("Ability (Noun): She has the ability to play the piano.", "Ability (İsim): Piyano çalma yeteneği var."),
("Able (Adjective): He's able to solve complex problems.", "Able (Sıfat): Karmaşık sorunları çözebilir."),
("About (Preposition): Let's talk about your vacation plans.", "About (Edat): Tatil planlarınızı konuşalım."),
("Above (Preposition): The stars are above us in the night sky.", "Above (Edat): Yıldızlar gece gökyüzümüzde."),
("Accept (Verb): They will accept the offer.", "Accept (Fiil): Teklifi kabul edecekler."),
("Accident (Noun): The car accident caused a lot of damage.", "Accident (İsim): Araba kazası büyük hasara neden oldu."),
("According to (Preposition): According to the weather forecast, it will rain tomorrow.", "According to (Edat): Hava tahminine göre yarın yağmur yağacak."),
("Account (Noun): I have a bank account at this branch.", "Account (İsim): Bu şubede bir banka hesabım var."),
("Across (Preposition): We walked across the bridge to the other side.", "Across (Edat): Köprüyü karşıya geçtik."),
("Act (Verb): She can act in both comedy and drama.", "Act (Fiil): Hem komedi hem de dramda rol alabilir."),
("Action (Noun): Taking action is important to achieve your goals.", "Action (İsim): Hedeflerinize ulaşmak için harekete geçmek önemlidir."),
("Active (Adjective): He leads an active lifestyle with lots of exercise.", "Active (Sıfat): Hareketli bir yaşam tarzı sürdürüyor, çok egzersiz yapıyor."),
("Activity (Noun): The school offers various extracurricular activities.", "Activity (İsim): Okul çeşitli ders dışı etkinlikler sunuyor."),
("Actor (Noun): He's a talented actor in Hollywood.", "Actor (İsim): Hollywood'da yetenekli bir aktör."),
("Actress (Noun): She's an award-winning actress.", "Actress (İsim): Ödüllü bir aktris."),
("Actually (Adverb): I didn't expect to see you here, actually.", "Actually (Zarf): Aslında seni burada görmeyi beklemiyordum."),
("Add (Verb): Can you add some sugar to the tea?", "Add (Fiil): Çaya biraz şeker ekleyebilir misin?"),
("Address (Noun/Verb): What's your home address? / He will address the issue in the meeting.", "Address (İsim/Fiil): Ev adresiniz nedir? / Sorunu toplantıda ele alacak."),
("Administration (Noun): The school administration handles student affairs.", "Administration (İsim): Okul yönetimi öğrenci işleriyle ilgilenir."),
("Admit (Verb): He had to admit his mistake.", "Admit (Fiil): Hatasını kabul etmek zorunda kaldı."),
("Adult (Noun/Adjective): She's an adult now. / Adult responsibilities come with freedom.", "Adult (İsim/Sıfat): Şimdi bir yetişkin. / Yetişkin sorumluluklar özgürlükle birlikte gelir."),
("Advertise (Verb): They advertise their products on television.", "Advertise (Fiil): Ürünlerini televizyonda reklam yapıyorlar."),
("Advertisement (Noun): I saw an advertisement for a new phone.", "Advertisement (İsim): Yeni bir telefon için reklam gördüm."),
("Advice (Noun): Can you give me some advice about traveling?", "Advice (İsim): Seyahat etmekle ilgili bazı tavsiyeler verebilir misin?"),
("Advise (Verb): I would advise you to reconsider.", "Advise (Fiil): Sana yeniden düşünmeni tavsiye ederim."),
("Afford (Verb): I can't afford to buy a new car right now.", "Afford (Fiil): Şu anda yeni bir araba alacak durumda değilim."),
("Afraid (Adjective): She's afraid of heights.", "Afraid (Sıfat): Yükseklikten korkuyor."),
("After (Preposition/Conjunction): We'll meet after the movie. / After she finished, we went for a walk.", "After (Edat/Zarf): Filmden sonra buluşacağız. / Bittiğinde yürüyüşe çıktık."),
("Again (Adverb): Let's try this again.", "Again (Zarf): Bunu tekrar deneyelim."),
("Against (Preposition): They competed against each other.", "Against (Edat): Birbirlerine karşı yarıştılar."),
("Age (Noun/Verb): What's your age? / As you age, your body changes.", "Age (İsim/Fiil): Kaç yaşındasın? / Yaşlandıkça vücudun değişir."),
("Agency (Noun): The travel agency arranged our vacation.", "Agency (İsim): Seyahat acentesi tatilimizi düzenledi."),
("Agent (Noun): He's a secret agent in the spy movie.", "Agent (İsim): Casus filmde gizli bir ajan."),
("Agree (Verb): We all agree with the plan.", "Agree (Fiil): Hepimiz plana katılıyoruz."),
("Agreement (Noun): They signed a legal agreement.", "Agreement (İsim): Yasal bir anlaşma imzaladılar."),
("Ahead (Adverb): The finish line is just ahead.", "Ahead (Zarf): Bitiş çizgisi hemen önümüzde."),
("Aid (Noun/Verb): The aid arrived quickly after the disaster. / Can you aid me with this task?", "Aid (İsim/Fiil): Yardım felaket sonrası hızla geldi. / Bu görevde bana yardım edebilir misin?"),
("Aim (Noun/Verb): What's your aim in life? / He aimed the arrow at the target.", "Aim (İsim/Fiil): Hayatta amacınız nedir? / Oku hedefe doğru yönlendirdi."),
("Air (Noun/Verb): Fresh air is invigorating. / The room needs to be aired out.", "Air (İsim/Fiil): Temiz hava canlandırıcıdır. / Odayı havalandırmak gerekiyor."),
("Aircraft (Noun): The airport is busy with various aircraft.", "Aircraft (İsim): Havalimanı çeşitli hava araçlarıyla dolu."),
("Airline (Noun): Which airline are you flying with?", "Airline (İsim): Hangi havayoluyla uçuyorsunuz?"),
("Airport (Noun): We'll meet you at the airport.", "Airport (İsim): Sizi havalimanında karşılayacağız."),
("Alarm (Noun/Verb): The alarm woke me up. / Don't alarm others unnecessarily.", "Alarm (İsim/Fiil): Alarm beni uyandırdı. / Diğerlerini gereksiz yere alarma geçirme."),
("Album (Noun): She released a new music album.", "Album (İsim): Yeni bir müzik albümü çıkardı."),
("Alcohol (Noun): He doesn't drink alcohol.", "Alcohol (İsim): Alkol içmez."),
("Alive (Adjective): The patient is alive and recovering.", "Alive (Sıfat): Hasta yaşıyor ve iyileşiyor."),
("All (Determiner/Adverb): All the students passed the exam. / I ate it all.", "All (Belirleyici/Zarf): Bütün öğrenciler sınavı geçti. / Hepsini yedim."),
("Allow (Verb): They allow pets in their apartment.", "Allow (Fiil): Dairelerinde evcil hayvanlara izin veriyorlar."),
("Almost (Adverb): She almost won the race.", "Almost (Zarf): Neredeyse yarışı kazanıyordu."),
("Alone (Adjective/Adverb): I prefer to be alone sometimes. / He traveled alone.", "Alone (Sıfat/Zarf): Bazen yalnız olmayı tercih ederim. / Tek başına seyahat etti."),
("Along (Preposition/Adverb): Walk along the path. / Bring a friend along.", "Along (Edat/Zarf): Yol boyunca yürüyün. / Bir arkadaşı yanına al."),
("Already (Adverb): She's already finished her work.", "Already (Zarf): O zaten işini bitirdi."),
("Also (Adverb): I like coffee, and I also like tea.", "Also (Zarf): Kahveyi seviyorum, aynı zamanda çayı da seviyorum."),
("Although (Conjunction): Although it rained, we still had fun.", "Although (Bağlaç): Yağmur yağmasına rağmen yine de eğlendik."),
("Always (Adverb): He's always on time.", "Always (Zarf): Her zaman zamanında gelir."),
("Amaze (Verb): Her performance amazed the audience.", "Amaze (Fiil): Onun performansı izleyicileri şaşırttı."),
("Amazing (Adjective): The view from the mountain top is amazing.", "Amazing (Sıfat): Dağın tepesinden görüntü inanılmaz."),
("Ambition (Noun): His ambition is to become a successful entrepreneur.", "Ambition (İsim): Onun hedefi başarılı bir girişimci olmak."),
("Ambitious (Adjective): She's an ambitious young professional.", "Ambitious (Sıfat): O, hırslı genç bir profesyonel.")
]


    def show_word(self):
        if self.words:
            self.english_label.config(text=self.words[self.index][0])
            self.translation_label.config(text="")

    def show_translation(self):
        if self.words:
            self.translation_label.config(text=self.words[self.index][1])

    def show_next_word(self):
        if self.words:
            self.index = (self.index + 1) % len(self.words)
            self.show_word()
            self.translation_label.config(text="")


root = tk.Tk()
app = VocabularyApp(root)
root.mainloop()
