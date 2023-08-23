'''
var els = document.getElementsByClassName("roster_user_name")
var names = [];
for (var i = 0; i<els.length; i++){ names.push(els[i].innerText)}
for (var i = 0; i<names.length; i++){
    names[i] = names[i].replace(" (He/Him)", " ")
    names[i] = names[i].replace(" (She/Her)", " ")
    names[i] = names[i].replace(" (They/Them)", " ")

     
     }


'''


names = [
    "Otabek Abduraufov ",
    "Tahmid Ahmed",
    "Mohamed Ahmed Al Kindi",
    "Faiz Alam",
    "Dariya Alibi",
    "Jason Barican",
    "Joshua Bernard",
    "Chloe Berry",
    "Joseph Beyrer",
    "Ameya Bhujbal",
    "Javier Cabanellas",
    "Victor Campisi",
    "Xianqi Cao",
    "Shivam Chauhan",
    "Matthew Chiaradio",
    "Grant Debiase",
    "Dakhari Ebanks",
    "Sergio Flores Rodriguez",
    "Sophie Garrett ",
    "Musa Al Sathman Gazi",
    "Matthew Gerken",
    "Ahmed Ghoneim",
    "Jian Gong",
    "David Hamilton",
    "Alexander Hatfield",
    "Darien Henrie",
    "Kayla Homatas ",
    "Sri Indukuri",
    "Timur Kalandarov",
    "Herbert Keels",
    "Tahsun Rahman Khan",
    "Ethan Kocses",
    "Venkata Rupesh Varma Konduru",
    "Adam Krause",
    "Vladislav Krukhmalev ",
    "Suraj Kumar",
    "Kaenan Lakheeram",
    "Chau Le",
    "Jimmy Le",
    "Ethan Leblanc",
    "Geoffroy Leyniers",
    "John Liu",
    "Lokanadhaya Maddula",
    "Hope Marcus",
    "Pedro Mir Reynoso",
    "Austin Molketin",
    "Anil Mumbuc ",
    "Anh Nguyen",
    "Faith Nittala",
    "Nischal Olety Nagesh "
]