m1 ="CRYPTANALYSIS IN RECENT PUBLICATIONS ALSO CRYPTANALYSISREFERS IN THE ORIGINAL SENSE TO THE STUDY OF METHODS ANDTECHNIQUES TO OBTAIN INFORMATION FROM SEALED TEXTS THISINFORMATION CAN BE BOTH THE KEY USED AND THE ORIGINAL TEXTNOWADAYS, THE TERM CRYPTANALYSIS MORE GENERALLY REFERS TOTHE ANALYSIS OF CRYPTOGRAPHIC METHODS NOT ONLY FOR CLOSUREWITH THE AIM OF EITHER BREAKING THEM I E ABOLISHING THEIRPROTECTIVE FUNCTION OR OR TO PROVE AND QUANTIFY THEIRSECURITY CRYPTANALYSIS IS THUS THE COUNTERPART TOCRYPTOGRAPHY BOTH ARE SUBFIELDS OF CRYPTOLOGY" 
m2 ="DIE KRYPTOANALYSE IN NEUEREN PUBLIKATIONEN AUCHKRYPTANALYSE BEZEICHNET IM URSPRUNGLICHEN SINNE DAS STUDIUMVON METHODEN UND TECHNIKEN UM INFORMATIONEN AUSVERSCHLUSSELTEN TEXTEN ZU GEWINNEN DIESE INFORMATIONENKONNEN SOWOHL DER VERWENDETE SCHLUSSEL ALS AUCH DERORIGINALTEXT SEIN HEUTZUTAGE BEZEICHNET DER BEGRIFFKRYPTOANALYSE ALLGEMEINER DIE ANALYSE VON KRYPTOGRAPHISCHENVERFAHREN NICHT NUR ZUR VERSCHLUSSELUNG MIT DEM ZIEL DIESEENTWEDER ZU BRECHEN D H IHRE SCHUTZFUNKTION AUFZUHEBEN BZWZU UMGEHEN ODER IHRE SICHERHEIT NACHZUWEISEN UND ZUQUANTIFIZIEREN KRYPTOANALYSE IST DAMIT DAS GEGENSTUCK ZURKRYPTOGRAPHIE BEIDE SIND TEILGEBIETE DER KRYPTOLOGIE"
m3 ="MVWZXYXEJIWGC ML BIAORR ZYZVMAKXGYRQ KPQY GPITRKRYVCQSWPOJCBW GX XFO SPSKGXEJ CILCI RY XFO WREHW YJ KOXFYHQ KRBDIARRGAYCC XM YFRKML SRDYVKKXGYR DBSK CIYVIB DIVDW RRMQSRDYVKKXGYR AKR ZO FMDL RRI IOC SCIB KRB DLC YVGQMLKP ROBRXSUKHYIW, RRI ROVK MVWZXYXEJIWGC QMBI EORCBEJVC POJCBW RYXFO ELKPWCMQ YJ ABCNDSEBENRMA WIRRSBC RMD SLVC DYV AVSQEVCGMRR XFO EGW SD OMRRIP LVCKOGXK RRIK S I YLSJSWFSRE DLCSVNBSROGRSZC PYLMXGYR MB SP DS NBSTO ELN USKRRSJW DLCSVQOGSBMRI GPITRKRYVCQSW GC XFEW RRI AYYLDIPZEPD XMMVWZXMQVYZLW LSRR EPO WSLJGOPBC SD MVWZXMVSEI"
m4 ="FUBSWDQDOBVLV LQ UHFHQW SXEOLFDWLRQV DOVR FUBSWDQDOBVLVUHIHUV LQ WKH RULJLQDO VHQVH WR WKH VWXGB RI PHWKRGV DQGWHFKQLTXHV WR REWDLQ LQIRUPDWLRQ IURP VHDOHG WHAWV WKLVLQIRUPDWLRQ FDQ EH ERWK WKH NHB XVHG DQG WKH RULJLQDO WHAWQRZDGDBV, WKH WHUP FUBSWDQDOBVLV PRUH JHQHUDOOB UHIHUV WRWKH DQDOBVLV RI FUBSWRJUDSKLF PHWKRGV QRW RQOB IRU FORVXUHZLWK WKH DLP RI HLWKHU EUHDNLQJ WKHP L H DEROLVKLQJ WKHLUSURWHFWLYH IXQFWLRQ RU RU WR SURYH DQG TXDQWLIB WKHLUVHFXULWB FUBSWDQDOBVLV LV WKXV WKH FRXQWHUSDUW WRFUBSWRJUDSKB ERWK DUH VXEILHOGV RI FUBSWRORJB" 
def coincidence(ciphertext):
    n = 0
    f = 0
    for i in range(26):
        fi = ciphertext.count(chr(ord('A') + i))+ciphertext.count(chr(ord('a') + i))
        n += fi
        f += fi * (fi-1)
    ans = float(f/(n*n-n))
    print(n)
    print(ans)
coincidence(m1)
coincidence(m2)
coincidence(m3)
coincidence(m4)