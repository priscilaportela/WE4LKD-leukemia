import nltk
import string

nltk.download('stopwords')
from nltk.corpus import stopwords 

stop_words = set(stopwords.words('english'))
personal_stop_words = ('rarα', 'aacr', 'aacs', 'aafc', 'aafp', 'aafps', 'aagm', 'aaipi', 'aalp',
                       'aamdsif', 'aame', 'aaml', 'aams', 'aamt', 'aapc', 
                       'aatc', 'aato', 'abcc', 'abcg', 'abcm', 'abfm', 'ablb', 'ablc', 'abmt',
                       'abmts', 'abvd', 'accs', 'acsdkp', 'acsl', 'acsls', 'acta', 'actb', 'actd',
                       'acted', 'actg', 'acth', 'actiii', 'acpd', 'adbw', 'adcc', 'adcp', 'adcr',
                       'adcs', 'advp', 'adzuki', 'aefp', 'ahas', 'ahbi', 'ahcc', 'ahct', 'ahead',
                       'ahfrt', 'ahnmd', 'ahnmds', 'ahsct', 'ahsp', 'aicar', 'aicda', 'aics', 'aida', 'aide'
                       'µmlchip', 'özen', 'černjavski', 'αenac', 'αgalcer', 'αiib', 'αsma', 'αβtcr',
                       'βcatenin', 'βphosphorylated', 'βtcr', 'δcak', 'δfret', 'δtcpc', 'μgrna', 'μmol', 'τhis')

fix_typos_dict = {'remarkablely': 'remarkably',
                  'leukaemia': 'leukemia',
                  'leukaemias': 'leukemias',
                  'efficiacy': 'efficiency',
}

##todo
#join words: Meridianin D = Meridianin-D#
#ara c : ara-c

for i in personal_stop_words:
    stop_words.add(i)

# define training data
summaries = [s.strip() for s in open("results_file.txt", encoding="utf-8")]

word_list = []
for s in summaries:
    s = s.split(' ')
    s = [word for word in s if word.isalpha()]
    s = [w.lower().translate({ord(x): '' for x in string.punctuation}) for w in s]
    #s = [w for w in s if len(w) >= 4]
    s = [w for w in s if not w in stop_words]
    s = [w if w not in fix_typos_dict else fix_typos_dict[w] for w in s]
    word_list.append(s)

res = list(map(' '.join, word_list))

with open("results_file_clean.txt", "w", encoding="utf-8") as outfile:
    outfile.write("\n".join(res))
