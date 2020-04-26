import GetOldTweets3 as got
#tweetCriteria = got.manager.TweetCriteria().setQuerySearch('i have the coronavirus').setMaxTweets(10)
handles = r"""@CarlyhudsonXx
@deray
@TiffanieWagner
@JessRiz
@sherlyholmes
@NoopurRajeMD
@MaggieAstor
@summberbrennan
@harmancipants
@j7eon
@leighluscious1
@ShirazMaher
@W_F_Thomas
@elizashapiro
@OMG_its_emilyx
@Mark_McClurg
@mirella_rangel
@may_chidiac
@danieldaekim
@arielepstein
@d_psycho_guru
@baeonda
@repbenmcadams
@kellyabagat
@RufusPeabody
@Dhodgem
@girlsreallyrule
@jasoncollins98
@bobakyunnie
@WOTB07
@karriehiggins
@technollama
@JaneMayMorrison
@MarkLevineNYC
@ObsoleteDogma
@LeeDuffy7
@atiku
@neil_ferguson
@fellaini
@algoulden
@ClementYChow
@LaurenGibsonMD
@JesseYisachar
@jigneshpatelMD
@theonlynyceguy
@mayyie_cheikh
@bradleyziffer
@DrJaninaRamirez
@MikeyCobban
@TimHerrera
@colleeenclarke
@kamrankbangash
@DarrinBMaxwell
@imhxneedy
@PRINZESKIM
@RealSteveH27
@shiraselko
@ANI
@janette_foggo
@JasonDunn16
@FriedBasballATL
@MatthewTabeek
@silv24
@stonecold2050
@_abbyhill__
@KnightLite95
@alyssamulkerrin
@hellochante
@JamesSkoufis
@JoSepH_1189
@delanetb__
@andreeeeezzzy
@nursedonwalker
@jesse_eb10
@LouSassle19
@EliKinsey
@ianq72
@jeffreestargive
@ParvatisHalien
@DamSourxe
@joannathemad89
@Borderlands3Key
@jamesgwriter
@OvernightRains
@taliverse
@BrightwoodBear
@kaitxspade
@robles567
@JordynHadden
@__AyeBrooks
@AngerierWHStaff
@TheBGKaptain
@JenWilson05
@LauraRiceli
@a_3p0
@TweetingYarnie
@nicolecmerhi
@ScheifferBates
@AoifeMoore01
@iancpix
@malego77
@TommyMurphy15
@Just_DeePotts
@Periwinkle896
@king_cayla
@Iamwanizubair
@bogorman1
@JooBilly
@johnjhargrove
@Arp14_
@nosheenhm
@marvinlwilliams
@YeardleyEmma
@ChrisCuomo
@smohomishweath1
@TanjieTheCoder
@AffordAnything
@sandofsky
@tydah_xo
@jdbftandrea
@MoniqueOMadan
@URIESBLUNT
@thewineforyouu
@SteelerDelivery
@soprano58_carol
@JillianSakovits
@Georgia_Hart_xx
@BorisJohnson
@shanmcdrmtt
@illini3sc
@Smoke_nd_Pearls
@tonywendice1954
@xXSJcraft99Xx
"""
import csv

usrs = [x.replace("@", "") for x in handles.split("\n")][:0]
data = []
labels = []
count = 0
for x in usrs:
    print(count/len(usrs))
    if len(x):
        tweetCriteria = got.manager.TweetCriteria().setUsername(x).setSince("2020-03-20").setMaxTweets(40)
        tweets = got.manager.TweetManager.getTweets(tweetCriteria)
        d = ""
        for tweet in tweets:
            d = d + " " + tweet.text
        if len(d):
            data.append(d)
            labels.append("positive")
        count += 1;
        
import GetOldTweets3 as got

tweetCriteria = got.manager.TweetCriteria().setQuerySearch("to").setSince("2020-03-20").setMaxTweets(150)
tweets = got.manager.TweetManager.getTweets(tweetCriteria)

handles2 = set()

count = 0

for tweet in tweets:
    handles2.add(tweet.username)

for x in handles2:
    print(count/len(handles2))
    if len(x):
        tweetCriteria = got.manager.TweetCriteria().setUsername(x).setSince("2020-03-20").setMaxTweets(20)
        tweets = got.manager.TweetManager.getTweets(tweetCriteria)
        d = ""
        for tweet in tweets:
            d = d + " " + tweet.text
        if len(d):
            data.append(d)
            labels.append("not positive")
        count += 1;
                
wtr = csv.writer(open ('out.csv', 'w', encoding="utf-8"), delimiter=',', lineterminator='\n')
for i in range(len(data)):
    wtr.writerow([data[i][min(1024, len(data[i]))], labels[i]])
