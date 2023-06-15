Komandrindiņas programma x.509 sertifikāta izveidošanai/pārbaudei un ziņojumu dekodēšanai/iekodēšanai.

Programma ir uzrakstīta valodā Python 3.10 un izmanto vairākas bibliotēkas tās darbības nodrošināšanai:
	- Crypto	Pycryptodome bibliotēka. Nodrošina iekodēšanu un atkodēšanu.
	- datetime	Sērijas numura aprēķināšanai.
	- json		Nolasa JSON formāta failus.
	- os		Tiek izmantots darbībām ar failiem.
	- sys		Pārtrauc programmas darbību, ja tiek sastapta tāda kļūda ievades datos, ka turpināt darbu nav vērts.
	- typing	Ļauj norādīt datu tipus funkcijām. Pirmkoda lasāmības uzlabošanai.
	
----
Darbs ar programmu:

0) Programmas palaišanai ir nepieciešams, lai uz datora būtu uzinstalēts Python 3.10. Iespējams, ka derēs arī citas Python 3 versijas, bet par to negalvoju. Gadījumā, ja programma izmet "ModuleNotFoundError" kļūdas paziņojumu, tad trūkstošo moduli var uzinstalēt ar 'pip install <module>' komandu.

1) Programmu palaiž caur komandrindiņu un lietotājs atlasa darbības opciju un faila vai failu nosaukumus, no kā tiks ielādēta informācija. Skatīt nākamo sadaļu par norādījumiem, kādā secībā faili ir ievadāmi.

2) Pēc uzdevuma izpildīšanas tiks saglabāti rezultātu faili mapē 'output' vai arī uz ekrāna tiks parādīts paziņojums.

----
Mapē 'input' ir iekļauti piemēri. 

Pirmajam uzdevuma solim:
 - input_01.json - Apraksta sertifikāta saturu. Šis fails tiek glabāts JSON formātā.

Otrajam uzdevuma solim - Sertifikāta un privātās atslēgas fails, kas izgatavots pirmajā solī:
 - 570608_CERTIFICATE.pem
 - 570608_KEY.pem

Trešajam uzdevuma solim - Iekodējama/dekodējama baitu virkne.
 - en_message.bin
 - de_message.bin
