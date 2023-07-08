"""
Japanese Vocabulary Trainer
Creator: Christopher Gettier

"""
from tkinter import *
# from tkinter.font import Font
# all of tkinter is imported and will be used to run the window
import random
# random is imported so rng can be used in the practice algorithms
import pyglet


# change source to a list so vocab can be included in multiple packs
# add 201

# make it look nicer
# make into executable　
# update writing trainer to include stroke order
# create real language generator for particle and reading practice
# users with user data
# verb modification


class Character:
    # This class is the template for the hiragana and katakana characters
    def __init__(self, char_type, character, romaji, num_correct=0):
        # string char_type determines whether the character is hiragana or katakana
        self.char_type = char_type
        # String that is the character
        self.character = character
        # String that is the romaji form of the character
        self.romaji = romaji
        # int that stores the amount of times in a row the user has correctly answered
        self.num_correct = num_correct


class Word:
    # This class represents words that will be studied in the vocab trainer, and includes member variables that both
    # sort and determine the words
    def __init__(self, word_type="", category="", subject="", english="", japanese="", source="", unit="",
                 kanji="", num_correct=0):
        # String that determines noun, adjective etc.
        self.type = word_type
        # A string value for sorting words
        self.category = category
        # An additional string value for sorting words
        self.subject = subject
        # string of the word in english
        self.english = english
        # string of the word in japanese
        self.japanese = japanese
        # source and unit determine places the word is used for reference
        self.source = source
        self.unit = unit
        # the number of times consecutively the user has correctly answered
        self.num_correct = num_correct
        self.first_attempt = True
        self.kanji = kanji


class Particle:
    # This class represents particles in the japanese language
    def __init__(self, character, uses):
        # A string of the hiragana character of the particle
        self.character = character
        # A list of strings that describe uses of the particle
        self.uses = uses


class Counter:
    # This class represents counters and number words in the Japanese language
    def __init__(self, japanese, english, num_type, kanji=""):
        # A string that is the hiragana or katakana representation of the counter word
        self.japanese = japanese
        # A string that is the english word for the counter
        self.english = english
        # A string that represents the type of number modification for the word
        self.num_type = num_type
        # A string that represents the kanji for the counter wor if one exists
        self.kanji = kanji


pyglet.font.add_file('IPAMincho Regular.ttf')

# list of the hiragana and katakana characters
char_list = [Character("hiragana", "あ", "a"),
             Character("hiragana", "い", "i"),
             Character("hiragana", "う", "u"),
             Character("hiragana", "え", "e"),
             Character("hiragana", "お", "o"),
             Character("hiragana", "か", "ka"),
             Character("hiragana", "き", "ki"),
             Character("hiragana", "く", "ku"),
             Character("hiragana", "け", "ke"),
             Character("hiragana", "こ", "ko"),
             Character("hiragana", "さ", "sa"),
             Character("hiragana", "し", "shi"),
             Character("hiragana", "す", "su"),
             Character("hiragana", "せ", "se"),
             Character("hiragana", "そ", "so"),
             Character("hiragana", "た", "ta"),
             Character("hiragana", "ち", "chi"),
             Character("hiragana", "つ", "tsu"),
             Character("hiragana", "て", "te"),
             Character("hiragana", "と", "to"),
             Character("hiragana", "な", "na"),
             Character("hiragana", "に", "ni"),
             Character("hiragana", "ぬ", "nu"),
             Character("hiragana", "ね", "ne"),
             Character("hiragana", "の", "no"),
             Character("hiragana", "は", "ha"),
             Character("hiragana", "ひ", "hi"),
             Character("hiragana", "ふ", "fu"),
             Character("hiragana", "へ", "he"),
             Character("hiragana", "ほ", "ho"),
             Character("hiragana", "ま", "ma"),
             Character("hiragana", "み", "mi"),
             Character("hiragana", "む", "mu"),
             Character("hiragana", "め", "me"),
             Character("hiragana", "も", "mo"),
             Character("hiragana", "や", "ya"),
             Character("hiragana", "ゆ", "yu"),
             Character("hiragana", "よ", "yo"),
             Character("hiragana", "ら", "ra"),
             Character("hiragana", "り", "ri"),
             Character("hiragana", "る", "ru"),
             Character("hiragana", "れ", "re"),
             Character("hiragana", "ろ", "ro"),
             Character("hiragana", "わ", "wa"),
             Character("hiragana", "を", "wo"),
             Character("hiragana", "ん", "n"),
             Character("hiragana", "が", "ga"),
             Character("mod hiragana", "ぎ", "gi"),
             Character("mod hiragana", "ぐ", "gu"),
             Character("mod hiragana", "げ", "ge"),
             Character("mod hiragana", "ご", "go"),
             Character("mod hiragana", "ざ", "za"),
             Character("mod hiragana", "じ", "ji"),
             Character("mod hiragana", "ず", "zu"),
             Character("mod hiragana", "ぜ", "ze"),
             Character("mod hiragana", "ぞ", "zo"),
             Character("mod hiragana", "だ", "da"),
             Character("mod hiragana", "で", "de"),
             Character("mod hiragana", "ど", "do"),
             Character("mod hiragana", "ば", "ba"),
             Character("mod hiragana", "び", "bi"),
             Character("mod hiragana", "ぶ", "bu"),
             Character("mod hiragana", "べ", "be"),
             Character("mod hiragana", "ぼ", "bo"),
             Character("mod hiragana", "ぱ", "pa"),
             Character("mod hiragana", "ぴ", "pi"),
             Character("mod hiragana", "ぷ", "pu"),
             Character("mod hiragana", "ぺ", "pe"),
             Character("mod hiragana", "ぽ", "po"),
             Character("comp hiragana", "きゃ", "kya"),
             Character("comp hiragana", "きゅ", "kyu"),
             Character("comp hiragana", "きょ", "kyo"),
             Character("comp hiragana", "しゃ", "sha"),
             Character("comp hiragana", "しゅ", "shu"),
             Character("comp hiragana", "しょ", "sho"),
             Character("comp hiragana", "ちゃ", "cha"),
             Character("comp hiragana", "ちゅ", "chu"),
             Character("comp hiragana", "ちょ", "cho"),
             Character("comp hiragana", "にゃ", "nya"),
             Character("comp hiragana", "にゅ", "nyu"),
             Character("comp hiragana", "にょ", "nyo"),
             Character("comp hiragana", "ひゃ", "hya"),
             Character("comp hiragana", "ひゅ", "hyu"),
             Character("comp hiragana", "ひょ", "hyo"),
             Character("comp hiragana", "みゃ", "mya"),
             Character("comp hiragana", "みゅ", "myu"),
             Character("comp hiragana", "みょ", "myo"),
             Character("comp hiragana", "りゃ", "rya"),
             Character("comp hiragana", "りゅ", "ryu"),
             Character("comp hiragana", "りょ", "ryo"),
             Character("comp hiragana", "ぎゃ", "gya"),
             Character("comp hiragana", "ぎゅ", "gyu"),
             Character("comp hiragana", "ぎょ", "gyo"),
             Character("comp hiragana", "じゃ", "ja"),
             Character("comp hiragana", "じゅ", "ju"),
             Character("comp hiragana", "じょ", "jo"),
             Character("comp hiragana", "びゃ", "bya"),
             Character("comp hiragana", "びゅ", "byu"),
             Character("comp hiragana", "びょ", "byo"),
             Character("comp hiragana", "ぴゃ", "pya"),
             Character("comp hiragana", "ぴゅ", "pyu"),
             Character("comp hiragana", "ぴょ", "pyo"),
             Character("katakana", "ア", "a"),
             Character("katakana", "イ", "i"),
             Character("katakana", "ウ", "u"),
             Character("katakana", "エ", "e"),
             Character("katakana", "オ", "o"),
             Character("katakana", "カ", "ka"),
             Character("katakana", "キ", "ki"),
             Character("katakana", "ク", "ku"),
             Character("katakana", "ケ", "ke"),
             Character("katakana", "コ", "ko"),
             Character("katakana", "サ", "sa"),
             Character("katakana", "シ", "shi"),
             Character("katakana", "ス", "su"),
             Character("katakana", "セ", "se"),
             Character("katakana", "ソ", "so"),
             Character("katakana", "タ", "ta"),
             Character("katakana", "チ", "chi"),
             Character("katakana", "ツ", "tsu"),
             Character("katakana", "テ", "te"),
             Character("katakana", "ト", "to"),
             Character("katakana", "ナ", "na"),
             Character("katakana", "ニ", "ni"),
             Character("katakana", "ヌ", "nu"),
             Character("katakana", "ネ", "ne"),
             Character("katakana", "ノ", "no"),
             Character("katakana", "ハ", "ha"),
             Character("katakana", "ヒ", "hi"),
             Character("katakana", "フ", "fu"),
             Character("katakana", "ヘ", "he"),
             Character("katakana", "ホ", "ho"),
             Character("katakana", "マ", "ma"),
             Character("katakana", "ミ", "mi"),
             Character("katakana", "ム", "mu"),
             Character("katakana", "メ", "me"),
             Character("katakana", "モ", "mo"),
             Character("katakana", "ヤ", "ya"),
             Character("katakana", "ユ", "yu"),
             Character("katakana", "ヨ", "yo"),
             Character("katakana", "ラ", "ra"),
             Character("katakana", "リ", "ri"),
             Character("katakana", "ル", "ru"),
             Character("katakana", "レ", "re"),
             Character("katakana", "ロ", "ro"),
             Character("katakana", "ワ", "wa"),
             Character("katakana", "ヲ", "wo"),
             Character("katakana", "ン", "n"),
             Character("mod katakana", "ガ", "ga"),
             Character("mod katakana", "ギ", "gi"),
             Character("mod katakana", "グ", "gu"),
             Character("mod katakana", "ゲ", "ge"),
             Character("mod katakana", "ゴ", "go"),
             Character("mod katakana", "ザ", "za"),
             Character("mod katakana", "ジ", "ji"),
             Character("mod katakana", "ズ", "zu"),
             Character("mod katakana", "ゼ", "ze"),
             Character("mod katakana", "ゾ", "zo"),
             Character("mod katakana", "ダ", "da"),
             Character("mod katakana", "デ", "de"),
             Character("mod katakana", "ド", "do"),
             Character("mod katakana", "バ", "ba"),
             Character("mod katakana", "ビ", "bi"),
             Character("mod katakana", "ブ", "bu"),
             Character("mod katakana", "ベ", "be"),
             Character("mod katakana", "ボ", "bo"),
             Character("mod katakana", "パ", "pa"),
             Character("mod katakana", "ピ", "pi"),
             Character("mod katakana", "プ", "pu"),
             Character("mod katakana", "ペ", "pe"),
             Character("mod katakana", "ポ", "po"),
             Character("comp katakana", "キャ", "kya"),
             Character("comp katakana", "キュ", "kyu"),
             Character("comp katakana", "キョ", "kyo"),
             Character("comp katakana", "シャ", "sha"),
             Character("comp katakana", "シュ", "shu"),
             Character("comp katakana", "シェ", "she"),
             Character("comp katakana", "ショ", "sho"),
             Character("comp katakana", "チャ", "cha"),
             Character("comp katakana", "チュ", "chu"),
             Character("comp katakana", "チェ", "che"),
             Character("comp katakana", "チョ", "cho"),
             Character("comp katakana", "ニャ", "nya"),
             Character("comp katakana", "ニュ", "nyu"),
             Character("comp katakana", "ニョ", "nyo"),
             Character("comp katakana", "ヒャ", "hya"),
             Character("comp katakana", "ヒュ", "hyu"),
             Character("comp katakana", "ヒョ", "hyo"),
             Character("comp katakana", "ミャ", "mya"),
             Character("comp katakana", "ミュ", "myu"),
             Character("comp katakana", "ミョ", "myo"),
             Character("comp katakana", "リャ", "rya"),
             Character("comp katakana", "リュ", "ryu"),
             Character("comp katakana", "リョ", "ryo"),
             Character("comp katakana", "ギャ", "gya"),
             Character("comp katakana", "ギュ", "gyu"),
             Character("comp katakana", "ギョ", "gyo"),
             Character("comp katakana", "ジャ", "ja"),
             Character("comp katakana", "ジュ", "ju"),
             Character("comp katakana", "ジェ", "je"),
             Character("comp katakana", "ジョ", "jo"),
             Character("comp katakana", "ビャ", "bya"),
             Character("comp katakana", "ビュ", "byu"),
             Character("comp katakana", "ビョ", "byo"),
             Character("comp katakana", "ピャ", "pya"),
             Character("comp katakana", "ピュ", "pyu"),
             Character("comp katakana", "ピョ", "pyo"),
             Character("rare katakana", "ウィ", "wi"),
             Character("rare katakana", "ウェ", "we"),
             Character("rare katakana", "ヲ", "wo"),
             Character("rare katakana", "クァ", "kwa"),
             Character("rare katakana", "クィ", "kwi"),
             Character("rare katakana", "クェ", "kwe"),
             Character("rare katakana", "クォ", "kwo"),
             Character("rare katakana", "ツァ", "tsa"),
             Character("rare katakana", "ツィ", "tsi"),
             Character("rare katakana", "ツェ", "tse"),
             Character("rare katakana", "ツォ", "tso"),
             Character("rare katakana", "ティ", "ti"),
             Character("rare katakana", "テュ", "tyu"),
             Character("rare katakana", "ファ", "fa"),
             Character("rare katakana", "フィ", "fi"),
             Character("rare katakana", "フュ", "fyu"),
             Character("rare katakana", "フェ", "fe"),
             Character("rare katakana", "フォ", "fo"),
             Character("rare katakana", "ディ", "di"),
             Character("rare katakana", "デュ", "dyu"),
             Character("rare katakana", "ヴァ", "va"),
             Character("rare katakana", "ヴィ", "vi"),
             Character("rare katakana", "ヴ", "vu"),
             Character("rare katakana", "ヴェ", "ve"),
             Character("rare katakana", "ヴォ", "vo")]

# The following is a list of all the words the trainer will use
vocab_list = [Word("noun", "person", "family", "father", "おとうさん", "101", "unit 1", "お父さん"),
              Word("noun", "person", "family", "mother", "おかあさん", "101", "unit 1", "お母さん"),
              Word("noun", "person", "family", "older brother", "おにいさん", "101", "unit 1", "お兄さん"),
              Word("noun", "person", "family", "younger brother", "おとうと", "101", "unit 1", "弟"),
              Word("noun", "person", "family", "older sister", "おねえさん", "101", "unit 1", "お姉さん"),
              Word("noun", "person", "family", "younger sister", "いもうと", "101", "unit 1", "妹"),
              Word("noun", "person", "family", "family", "かぞく", "101", "unit 1", "家族"),
              Word("noun", "person", "family", "grandfather", "おじいさん", "102", "unit 7"),
              Word("noun", "person", "family", "grandmother", "おばあさん", "102", "unit 7"),
              Word("noun", "person", "family", "my father", "ちち", "102", "unit 7", "父"),
              Word("noun", "person", "family", "my mother", "はは", "102", "unit 7", "母"),
              Word("noun", "person", "family", "my older brother", "あに", "102", "unit 7", "兄"),
              Word("noun", "person", "family", "my older sister", "あね", "102", "unit 7", "姉"),
              Word("noun", "person", "family", "siblings", "きょうだい", "102", "unit 7", "兄弟"),
              Word("noun", "person", "family", "host family", "ホストファミリー", "102", "unit 11"),
              Word("noun", "person", "family", "husband", "ごしゅじん", "102", "bonus 1", "ご主人"),
              Word("noun", "person", "family", "wife", "おくさん", "102", "bonus 1", "奥さん"),
              Word("noun", "person", "family", "my husband", "おっと", "102", "bonus 1", "夫"),
              Word("noun", "person", "family", "my wife", "つま", "102", "bonus 1", "妻"),
              Word("noun", "person", "family", "my grandfather", "そふ", "102", "bonus 1", "祖父"),
              Word("noun", "person", "family", "my grandmother", "そぼ", "102", "bonus 1", "祖母"),
              Word("noun", "person", "school", "teacher", "せんせい", "101", "unit 1", "先生"),
              Word("noun", "person", "school", "student", "がくせい", "101", "unit 1", "学生"),
              Word("noun", "person", "school", "college student", "だいがくせい", "101", "unit 1", "大学生"),
              Word("noun", "person", "school", "international student", "りゅうがくせい", "101", "unit 1"),
              Word("noun", "person", "school", "first year student", "いちねんせい", "101", "unit 1", "一年生"),
              Word("noun", "person", "school", "second year student", "にねんせい", "101", "unit 1", "二年生"),
              Word("noun", "person", "school", "third year student", "さんねんせい", "101", "unit 1", "三年生"),
              Word("noun", "person", "school", "fourth year student", "よんねんせい", "101", "unit 1", "四年生"),
              Word("noun", "person", "school", "high school student", "こうこうせい", "101", "unit 1", "高校生"),
              Word("noun", "person", "school", "graduate student", "だいがくいんせい", "101", "unit 1"),
              Word("noun", "person", "occupation", "doctor", "いしゃ", "101", "unit 1", "医者"),
              Word("noun", "person", "occupation", "office worker", "かいしゃいん", "101", "unit 1", "会社員"),
              Word("noun", "person", "occupation", "nurse", "かんごし", "101", "unit 1", "看護師"),
              Word("noun", "person", "occupation", "housewife", "しゅふ", "101", "unit 1"),
              Word("noun", "person", "occupation", "lawyer", "べんごし", "101", "unit 1"),
              Word("noun", "person", "occupation", "occupation", "しごと", "101", "unit 1", "仕事"),
              Word("noun", "person", "occupation", "singer", "かしゅ", "102", "unit 11", "歌手"),
              Word("noun", "person", "occupation", "president of a company", "しゃちょう", "102", "unit 11", "社長"),
              Word("noun", "person", "occupation", "writer", "さっか", "102", "unit 11", "作家"),
              Word("noun", "person", "occupation", "journalist", "ジャーナリスト", "102", "unit 11"),
              Word("noun", "person", "occupation", "police officer", "けいさつかん", "102", "unit 11", "警察官"),
              Word("noun", "person", "occupation", "firefighter", "しょうぼうし", "102", "unit 11", "消防士"),
              Word("noun", "person", "occupation", "schoolteacher", "きょうし", "102", "unit 11", "教師"),
              Word("noun", "person", "occupation", "researcher", "けんきゅうしゃ", "102", "unit 11", "研究者"),
              Word("noun", "person", "occupation", "astronaut", "うちゅうひこうし", "102", "unit 11", "宇宙飛行士"),
              Word("noun", "person", "occupation", "athlete", "スポーツせんしゅ", "102", "unit 11", "スポーツ選手"),
              Word("noun", "person", "occupation", "president of a country", "だいとうりょう", "102", "unit 11", "大統領"),
              Word("noun", "person", "occupation", "actor", "はいゆう", "102", "unit 11", "俳優"),
              Word("noun", "person", "occupation", "chef", "シェフ", "102", "unit 11"),
              Word("noun", "person", "occupation", "cartoonist", "まんがか", "102", "unit 11", "漫画家"),
              Word("noun", "person", "nationality", "japanese person", "にほんじん", "101", "unit 1", "日本人"),
              Word("noun", "person", "nationality", "american person", "アメリカじん", "101", "unit 1"),
              Word("noun", "person", "other", "friend", "ともだち", "101", "unit 1", "友だち"),
              Word("noun", "person", "other", "person", "ひと", "101", "unit 4", "人"),
              Word("noun", "person", "other", "child", "こども", "101", "unit 4", "子供"),
              Word("noun", "person", "other", "man", "おとこのひと", "102", "unit 7", "男の人"),
              Word("noun", "person", "other", "woman", "おんなのひと", "102", "unit 7", "女の子"),
              Word("noun", "person", "other", "good child", "いいこ", "102", "unit 9", "いい子"),
              Word("noun", "person", "other", "rich person", "おかねもち", "102", "unit 10", "お金持ち"),
              Word("noun", "person", "other", "celebrity", "ゆうめいじん", "102", "unit 10", "有名人"),
              Word("noun", "person", "other", "someone older", "としうえ", "102", "unit 10", "年上"),
              Word("noun", "person", "other", "this person", "こちら", "102", "unit 11"),
              Word("noun", "person", "other", "roommate", "ルームメイト", "102", "unit 11"),
              Word("noun", "person", "other", "she/girlfriend", "かのじょ", "102", "unit 12", "彼女"),
              Word("noun", "person", "other", "he/boyfriend", "かれ", "102", "unit 12", "彼"),
              Word("noun", "person", "other", "boyfriend", "かれし", "102", "unit 12", "彼氏"),
              Word("noun", "person", "other", "physician", "ないか", "102", "bonus 1", "内科"),
              Word("noun", "person", "other", "dermatologist", "ひふか", "102", "bonus 1", "皮膚科"),
              Word("noun", "person", "other", "surgeon", "げか", "102", "bonus 1", "外科"),
              Word("noun", "person", "other", "dentist", "しか", "102", "bonus 1", "歯科"),
              Word("noun", "place", "biome", "university", "だいがく", "101", "unit 1", "大学"),
              Word("noun", "place", "building", "high school", "こうこう", "101", "unit 1", "高校"),
              Word("noun", "place", "building", "home", "いえ", "101", "unit 3", "家"),
              Word("noun", "place", "building", "restaurant", "レストラン", "101", "unit 4"),
              Word("noun", "place", "building", "store", "みせ", "100", "unit 2"),
              Word("noun", "place", "building", "my place", "うち", "100", "unit 3"),
              Word("noun", "place", "building", "cafe", "カフェ", "100", "unit 3"),
              Word("noun", "place", "building", "school", "がっこう", "101", "unit 3", "学校"),
              Word("noun", "place", "building", "hospital", "びょういん", "101", "unit 4", "病院"),
              Word("noun", "place", "building", "bank", "ぎんこう", "101", "unit 2"),
              Word("noun", "place", "building", "temple", "おてら", "101", "unit 4", "お寺"),
              Word("noun", "place", "building", "supermarket", "スーパー", "101", "unit 4"),
              Word("noun", "place", "building", "hotel", "ホテル", "101", "unit 4"),
              Word("noun", "place", "building", "bookstore", "ほんや", "101", "unit 4", "本屋"),
              Word("noun", "place", "building", "convenience store", "コンビニ", "101", "unit 2"),
              Word("noun", "place", "building", "department store", "デパート", "102", "unit 7"),
              Word("noun", "place", "building", "beauty parlor", "びよういん", "102", "unit 10", "美容院"),
              Word("noun", "place", "building", "library", "としょかん", "101", "unit 2"),
              Word("noun", "place", "building", "post office", "ゆうびんきょく", "101", "unit 2"),
              Word("noun", "place", "building", "art museum", "びじゅつかん", "102", "unit 11", "美術館"),
              Word("noun", "place", "country", "britain", "イギリス", "101", "unit 1"),
              Word("noun", "place", "country", "australia", "オーストラリア", "101", "unit 1"),
              Word("noun", "place", "country", "canada", "カナダ", "101", "unit 1"),
              Word("noun", "place", "country", "india", "インド", "101", "unit 1"),
              Word("noun", "place", "country", "egypt", "エジプト", "101", "unit 1"),
              Word("noun", "place", "country", "philippines", "フィリピン", "101", "unit 1"),
              Word("noun", "place", "country", "japan", "にほん", "101", "unit 1", "日本"),
              Word("noun", "place", "country", "united states", "アメリカ", "101", "unit 1"),
              Word("noun", "place", "country", "korea", "かんこく", "101", "unit 1"),
              Word("noun", "place", "country", "country", "くに", "101", "unit 1", "国"),
              Word("noun", "place", "country", "china", "ちゅうごく", "101", "unit 1"),
              Word("noun", "place", "country", "spain", "スペイン", "102", "unit 8"),
              Word("noun", "place", "country", "foreign country", "がいこく", "102", "unit 11", "外国"),
              Word("noun", "place", "room", "restroom", "トイレ", "101", "unit 2"),
              Word("noun", "place", "room", "cafeteria", "しょくどう", "102", "unit 7", "食堂"),
              Word("noun", "place", "room", "room", "へや", "101", "unit 5", "部屋"),
              Word("noun", "place", "room", "restroom", "おてあらい", "102", "unit 12", "お手洗い"),
              Word("noun", "place", "biome", "town", "まち", "101", "unit 4", "町"),
              Word("noun", "place", "biome", "sea", "うみ", "101", "unit 5", "海"),
              Word("noun", "place", "biome", "river", "かわ", "102", "unit 11", "川"),
              Word("noun", "place", "biome", "lake", "みずうみ", "102", "unit 11", "湖"),
              Word("noun", "place", "biome", "mountain", "やま", "102", "unit 11", "山"),
              Word("noun", "place", "other", "park", "こうえん", "101", "unit 4", "公園"),
              Word("noun", "place", "other", "bus stop", "バスてい", "101", "unit 4", "バス停"),
              Word("noun", "place", "other", "place", "ところ", "102", "unit 8", "所"),
              Word("noun", "place", "other", "station", "えき", "102", "unit 10", "駅"),
              Word("noun", "place", "other", "subway", "ちかてつ", "102", "unit 10", "地下鉄"),
              Word("noun", "place", "other", "zoo", "どうぶつえん", "102", "unit 10", "動物園"),
              Word("noun", "place", "other", "world", "せかい", "102", "unit 10", "世界"),
              Word("noun", "place", "other", "spa/hot spring", "おんせん", "102", "unit 11", "温泉"),
              Word("noun", "place", "other", "camp", "キャンプ", "102", "unit 11"),
              Word("noun", "place", "other", "shrine", "じんじゃ", "102", "unit 11", "神社"),
              Word("noun", "place", "other", "ticket vending area", "きっぷうりば", "102", "bonus 1", "切符売り場"),
              Word("noun", "place", "other", "gate (train)", "かいさつ", "102", "bonus 1", "改札"),
              Word("noun", "place", "other", "platform (train)", "ホーム", "102", "bonus 1"),
              Word("noun", "place", "other", "shop/stand", "ばいてん", "102", "bonus 1", "売店"),
              Word("noun", "place", "other", "exit", "でぐち", "102", "bonus 1", "出口"),
              Word("noun", "place", "other", "entrance", "入口", "102", "bonus 1", "神社"),
              Word("noun", "place", "other", "stairs", "かいだん", "102", "bonus 1", "階段"),
              Word("noun", "thing", "clothes", "t-shirt", "ティーシャツ", "101", "unit 2"),
              Word("noun", "thing", "clothes", "watch", "とけい", "101", "unit 2"),
              Word("noun", "thing", "clothes", "shoe", "くつ", "101", "unit 2"),
              Word("noun", "thing", "clothes", "jeans", "ジーンズ", "101", "unit 2"),
              Word("noun", "thing", "clothes", "hat", "ぼうし", "101", "unit 2"),
              Word("noun", "thing", "clothes", "gloves", "てぶくろ", "102", "unit 10", "手袋"),
              Word("noun", "thing", "clothes", "clothes", "ふく", "102", "unit 12", "服"),
              Word("noun", "thing", "furniture", "chair", "いす", "101", "unit 4"),
              Word("noun", "thing", "furniture", "desk", "つくえ", "101", "unit 4", "机"),
              Word("noun", "thing", "furniture", "bath", "おふろ", "102", "unit 8", "お風呂"),
              Word("noun", "thing", "major", "major", "せんこう", "101", "unit 1"),
              Word("noun", "thing", "major", "english", "えいご", "101", "unit 2"),
              Word("noun", "thing", "major", "asian studies", "アジアけんきゅう", "101", "unit 1"),
              Word("noun", "thing", "major", "economics", "けいざい", "101", "unit 1"),
              Word("noun", "thing", "major", "engineering", "こうがく", "101", "unit 1"),
              Word("noun", "thing", "major", "computer", "コンピューター", "101", "unit 1"),
              Word("noun", "thing", "major", "politics", "せいじ", "101", "unit 1", "政治"),
              Word("noun", "thing", "major", "biology", "せいぶつがく", "101", "unit 1"),
              Word("noun", "thing", "major", "business", "ビジネス", "101", "unit 1"),
              Word("noun", "thing", "major", "literature", "ぶんがく", "101", "unit 1", "文学"),
              Word("noun", "thing", "major", "history", "れきし", "101", "unit 1"),
              Word("noun", "thing", "major", "international relations", "こくさいかんけい", "101", "unit 1"),
              Word("noun", "thing", "technology", "telephone", "でんわ", "101", "unit 1", "電話"),
              Word("noun", "thing", "technology", "smart phone", "スマホ", "101", "unit 2"),
              Word("noun", "thing", "technology", "camera", "カメラ", "102", "unit 8"),
              Word("noun", "thing", "food", "fish", "さかな", "101", "unit 2"),
              Word("noun", "thing", "food", "food", "たべもの", "101", "unit 5", "食べ物"),
              Word("noun", "thing", "food", "drink", "のみもの", "101", "unit 5", "飲み物"),
              Word("noun", "thing", "food", "fruit", "くだもの", "101", "unit 5", "果物"),
              Word("noun", "thing", "food", "pork cutlet", "とんかつ", "101", "unit 2"),
              Word("noun", "thing", "food", "meat", "にく", "101", "unit 2"),
              Word("noun", "thing", "food", "ice cream", "アイスクリーム", "101", "unit 3"),
              Word("noun", "thing", "food", "hamburger", "ハンバーガー", "101", "unit 3"),
              Word("noun", "thing", "food", "alcohol", "おさけ", "101", "unit 3", "お酒"),
              Word("noun", "thing", "food", "green tea", "おちゃ", "101", "unit 3", "お茶"),
              Word("noun", "thing", "food", "coffee", "コーヒー", "101", "unit 3"),
              Word("noun", "thing", "food", "water", "みず", "101", "unit 3", "水"),
              Word("noun", "thing", "food", "breakfast", "あさごはん", "101", "unit 3", "朝ご飯"),
              Word("noun", "thing", "food", "lunch", "ひるごはん", "101", "unit 3", "昼ご飯"),
              Word("noun", "thing", "food", "dinner", "ばんごはん", "101", "unit 3", "晩ご飯"),
              Word("noun", "thing", "food", "rice", "ごはん", "101", "unit 4", "ご飯"),
              Word("noun", "thing", "food", "bread", "パン", "101", "unit 4"),
              Word("noun", "thing", "food", "menu", "メニュー", "101", "unit 2"),
              Word("noun", "thing", "food", "vegetables", "やさい", "101", "unit 2"),
              Word("noun", "thing", "food", "barbecue", "バーベキュー", "102", "unit 8"),
              Word("noun", "thing", "food", "tomato", "トマト", "102", "unit 8"),
              Word("noun", "thing", "food", "chopsticks", "はし", "102", "unit 8"),
              Word("noun", "thing", "food", "boxed lunch", "おべんとう", "102", "unit 9", "お弁当"),
              Word("noun", "thing", "food", "pizza", "ピザ", "102", "unit 9"),
              Word("noun", "thing", "food", "milk", "ぎゅうにゅう", "102", "unit 10", "牛乳"),
              Word("noun", "thing", "food", "cake", "ケーキ", "102", "unit 10"),
              Word("noun", "thing", "food", "sushi", "すし", "102", "unit 10"),
              Word("noun", "thing", "food", "tempura", "てんぷら", "102", "unit 10", "天ぷら"),
              Word("noun", "thing", "food", "apple", "りんご", "102", "unit 10"),
              Word("noun", "thing", "food", "cuisine", "りょうり", "102", "unit 10", "料理"),
              Word("noun", "thing", "food", "beer", "ビール", "102", "unit 11"),
              Word("noun", "thing", "food", "snack", "おかし", "102", "unit 11", "お菓子"),
              Word("noun", "thing", "food", "juice", "ジュース", "102", "unit 12"),
              Word("noun", "thing", "food", "egg", "たまご", "102", "unit 12", "卵"),
              Word("noun", "thing", "food", "strawberry", "いちご", "102", "bonus 1"),
              Word("noun", "thing", "food", "watermelon", "すいか", "102", "bonus 1"),
              Word("noun", "thing", "food", "mandarin orange", "みかん", "102", "bonus 1"),
              Word("noun", "thing", "food", "peach", "もも", "102", "bonus 1"),
              Word("noun", "thing", "food", "grape", "ぶどう", "102", "bonus 1"),
              Word("noun", "thing", "food", "carrot", "にんじん", "102", "bonus 1"),
              Word("noun", "thing", "food", "onion", "たまねぎ", "102", "bonus 1"),
              Word("noun", "thing", "food", "potato", "じゃがいも", "102", "bonus 1"),
              Word("noun", "thing", "food", "eggplant", "なす", "102", "bonus 1"),
              Word("noun", "thing", "food", "cucumber", "きゅうり", "102", "bonus 1"),
              Word("noun", "thing", "food", "cabbage", "キャベツ", "102", "bonus 1"),
              Word("noun", "thing", "food", "beef", "ぎゅうにく", "102", "bonus 1", "牛肉"),
              Word("noun", "thing", "food", "pork", "ぶたにく", "102", "bonus 1", "豚肉"),
              Word("noun", "thing", "food", "chicken meat", "とりにく", "102", "bonus 1", "鶏肉"),
              Word("noun", "thing", "food", "side dish", "おかず", "102", "bonus 1"),
              Word("noun", "thing", "food", "soup", "みそしる", "102", "bonus 1", "みそ汁"),
              Word("noun", "thing", "food", "set menu", "ていしょく", "102", "bonus 1", "定食"),
              Word("noun", "thing", "food", "dumplings", "ぎょうざ", "102", "bonus 1"),
              Word("noun", "thing", "food", "beef rice bowl", "ぎゅうどん", "102", "bonus 1", "牛丼"),
              Word("noun", "thing", "food", "pancake", "おこのみやき", "102", "bonus 1", "お好み焼き"),
              Word("noun", "thing", "food", "rice balls", "おにぎり", "102", "bonus 1"),
              Word("noun", "thing", "entertainment", "movie", "えいが", "101", "unit 3", "映画"),
              Word("noun", "thing", "entertainment", "music", "おんがく", "101", "unit 3", "音楽"),
              Word("noun", "thing", "entertainment", "magazine", "ざっし", "101", "unit 3", "雑誌"),
              Word("noun", "thing", "entertainment", "sports", "スポーツ", "101", "unit 3"),
              Word("noun", "thing", "entertainment", "date", "デート", "101", "unit 3"),
              Word("noun", "thing", "entertainment", "tennis", "テニス", "101", "unit 3"),
              Word("noun", "thing", "entertainment", "television", "テレビ", "101", "unit 3"),
              Word("noun", "thing", "entertainment", "karaoke", "カラオケ", "102", "unit 8"),
              Word("noun", "thing", "entertainment", "party", "パーティー", "102", "unit 8"),
              Word("noun", "thing", "entertainment", "concert", "コンサート", "102", "unit 9"),
              Word("noun", "thing", "entertainment", "kabuki", "かぶき", "102", "unit 9", "歌舞伎"),
              Word("noun", "thing", "entertainment", "soccer", "サッカー", "102", "unit 10"),
              Word("noun", "thing", "entertainment", "baseball", "やきゅう", "102", "unit 10", "野球"),
              Word("noun", "thing", "entertainment", "festival", "おまつり", "102", "unit 11", "お祭り"),
              Word("noun", "thing", "entertainment", "toy", "おもちゃ", "102", "unit 11"),
              Word("noun", "thing", "entertainment", "match/game", "しあい", "102", "unit 12", "試合"),
              Word("noun", "thing", "time", "tomorrow", "あした", "101", "unit 3", "明日"),
              Word("noun", "thing", "time", "today", "きょう", "101", "unit 3", "今日"),
              Word("noun", "thing", "time", "yesterday", "きのう", "101", "unit 4", "昨日"),
              Word("noun", "thing", "time", "hours", "じかん", "101", "unit 4", "時間"),
              Word("noun", "thing", "time", "last week", "せんしゅう", "101", "unit 4", "先週"),
              Word("noun", "thing", "time", "this week", "こんしゅう", "101", "unit 6", "今週"),
              Word("noun", "thing", "time", "next week", "らいしゅう", "101", "unit 6", "来週"),
              Word("noun", "thing", "time", "next year", "らいねん", "101", "unit 6", "来年"),
              Word("noun", "thing", "time", "night", "よる", "101", "unit 6", "夜"),
              Word("noun", "thing", "time", "morning", "あさ", "101", "unit 3", "朝"),
              Word("noun", "thing", "time", "tonight", "こんばん", "101", "unit 3", "今晩"),
              Word("noun", "thing", "time", "every day", "まいにち", "101", "unit 3", "毎日"),
              Word("noun", "thing", "time", "every night", "まいばん", "101", "unit 3", "毎晩"),
              Word("noun", "thing", "time", "weekend", "しゅうまつ", "101", "unit 3", "週末"),
              Word("noun", "thing", "time", "saturday", "どようび", "101", "unit 3", "土曜日"),
              Word("noun", "thing", "time", "sunday", "にちようび", "101", "unit 3", "日曜日"),
              Word("noun", "thing", "time", "monday", "げつようび", "101", "unit 4", "月曜日"),
              Word("noun", "thing", "time", "tuesday", "かようび", "101", "unit 4", "火曜日"),
              Word("noun", "thing", "time", "wednesday", "すいようび", "101", "unit 4", "水曜日"),
              Word("noun", "thing", "time", "thursday", "もくようび", "101", "unit 4", "木曜日"),
              Word("noun", "thing", "time", "friday", "きんようび", "101", "unit 4", "金曜日"),
              Word("noun", "thing", "time", "holiday", "やすみ", "101", "unit 5", "休み"),
              Word("noun", "thing", "time", "birthday", "たんじょうび", "101", "unit 5", "誕生日"),
              Word("noun", "thing", "time", "summer", "なつ", "102", "unit 8", "夏"),
              Word("noun", "thing", "time", "winter", "ふゆ", "102", "unit 8", "冬"),
              Word("noun", "thing", "time", "this morning", "けさ", "102", "unit 8", "今朝"),
              Word("noun", "thing", "time", "the day after tomorrow", "あさって", "102", "unit 8"),
              Word("noun", "thing", "time", "every week", "まいしゅう", "102", "unit 8", "毎週"),
              Word("noun", "thing", "time", "this month", "こんげつ", "102", "unit 8", "今月"),
              Word("noun", "thing", "time", "next month", "らいげつ", "102", "unit 8", "来月"),
              Word("noun", "thing", "time", "near future", "こんど", "102", "unit 9", "今度"),
              Word("noun", "thing", "time", "last month", "せんげつ", "102", "unit 9", "先月"),
              Word("noun", "thing", "time", "last year", "きょねん", "102", "unit 9", "去年"),
              Word("noun", "thing", "time", "season", "きせつ", "102", "unit 10", "季節"),
              Word("noun", "thing", "time", "spring", "はる", "102", "unit 10", "春"),
              Word("noun", "thing", "time", "fall", "あき", "102", "unit 10", "秋"),
              Word("noun", "thing", "time", "time", "じかん", "102", "unit 10", "時間"),
              Word("noun", "thing", "time", "this year", "ことし", "102", "unit 10", "今年"),
              Word("noun", "thing", "time", "this semester", "こんがっき", "102", "unit 11", "今学期"),
              Word("noun", "thing", "time", "next semester", "らいがっき", "102", "unit 11", "来学期"),
              Word("noun", "thing", "time", "New Year's", "おしょうがつ", "102", "unit 11", "お正月"),
              Word("noun", "thing", "time", "future", "しょうらい", "102", "unit 11", "将来"),
              Word("noun", "thing", "time", "New Year's Day", "がんじつ", "102", "bonus 1", "元日"),
              Word("noun", "thing", "time", "Coming-Of-Age Day", "せいじんのひ", "102", "bonus 1", "成人の日"),
              Word("noun", "thing", "time", "National Foundation Day", "けんこくきねんのひ", "102", "bonus 1", "建国記念の日"),
              Word("noun", "thing", "time", "Emperor's Birthday", "てんのたんじょうび", "102", "bonus 1", "天の誕生日"),
              Word("noun", "thing", "time", "Vernal Equinox Day", "しゅんぶんのひ", "102", "bonus 1", "春分の日"),
              Word("noun", "thing", "time", "Showa Day", "しょうわのひ", "102", "bonus 1", "昭和の日"),
              Word("noun", "thing", "time", "Constitution Day", "けんぽうきねんび", "102", "bonus 1", "憲法記念日"),
              Word("noun", "thing", "time", "Greenery Day", "みどりのひ", "102", "bonus 1", "みどりの日"),
              Word("noun", "thing", "time", "Children's Day", "こどものひ", "102", "bonus 1", "こどもの日"),
              Word("noun", "thing", "time", "Marine Day", "うみのひ", "102", "bonus 1", "海の日"),
              Word("noun", "thing", "time", "Mountain Day", "やまのひ", "102", "bonus 1", "山の日"),
              Word("noun", "thing", "time", "Respect-for-the-Aged Day", "けいろうのひ", "102", "bonus 1", "敬老の日"),
              Word("noun", "thing", "time", "Autumnal Equinox Day", "しゅうぶんのひ", "102", "bonus 1", "秋分の日"),
              Word("noun", "thing", "time", "Health and Sports Day", "スポーツのひ", "102", "bonus 1", "スポーツの日"),
              Word("noun", "thing", "time", "Culture Day", "ぶんかのひ", "102", "bonus 1", "文化の日"),
              Word("noun", "thing", "time", "Labor Thanksgiving Day", "きんろうかんしゃのひ", "102", "bonus 1", "勤労感謝の日"),
              Word("noun", "thing", "time", "the day before yesterday", "おととい", "102", "bonus 1"),
              Word("noun", "thing", "time", "two weeks ago", "にしゅうかんまえ", "102", "bonus 1", "二週間前"),
              Word("noun", "thing", "time", "two months ago", "にかげつまえ", "102", "bonus 1", "二か月間"),
              Word("noun", "thing", "time", "the year before last", "おととし", "102", "bonus 1"),
              Word("noun", "thing", "time", "the week after next", "さらいしゅう", "102", "bonus 1", "再来週"),
              Word("noun", "thing", "time", "the month after next", "さらいげつ", "102", "bonus 1", "再来月"),
              Word("noun", "thing", "time", "the year after next", "さらいねん", "102", "bonus 1", "再来年"),
              Word("noun", "thing", "time", "summer vacation", "なつやすみ", "102", "bonus 1", "夏休み"),
              Word("noun", "thing", "time", "winter vacation", "ふゆやすみ", "102", "bonus 1", "冬休み"),
              Word("noun", "thing", "time", "spring vacation", "はるやすみ", "102", "bonus 1", "春休み"),
              Word("noun", "thing", "animal", "dog", "いぬ", "101", "unit 4", "犬"),
              Word("noun", "thing", "animal", "cat", "ねこ", "101", "unit 4", "猫"),
              Word("noun", "thing", "other", "number", "ばんごう", "101", "unit 1"),
              Word("noun", "thing", "other", "name", "なまえ", "101", "unit 1", "名前"),
              Word("noun", "thing", "other", "umbrella", "かさ", "101", "unit 2"),
              Word("noun", "thing", "other", "bag", "かばん", "101", "unit 2"),
              Word("noun", "thing", "other", "wallet", "さいふ", "101", "unit 2"),
              Word("noun", "thing", "other", "bicycle", "じてんしゃ", "101", "unit 2"),
              Word("noun", "thing", "other", "newspaper", "しんぶん", "101", "unit 2", "新聞"),
              Word("noun", "thing", "other", "notebook", "ノート", "101", "unit 2"),
              Word("noun", "thing", "other", "pen", "ぺん", "101", "unit 2"),
              Word("noun", "thing", "other", "book", "ほん", "101", "unit 2", "本"),
              Word("noun", "thing", "other", "this one", "これ", "101", "unit 2"),
              Word("noun", "thing", "other", "that one", "それ", "101", "unit 2"),
              Word("noun", "thing", "other", "that one over there", "あれ", "101", "unit 2"),
              Word("noun", "thing", "other", "yen", "えん", "101", "unit 2", "円"),
              Word("noun", "thing", "other", "game", "ゲーム", "101", "unit 4"),
              Word("noun", "thing", "other", "class", "クラス", "101", "unit 4"),
              Word("noun", "thing", "other", "shopping", "かいもの", "101", "unit 4", "買い物"),
              Word("noun", "thing", "other", "part-time job", "アルバイト", "101", "unit 4"),
              Word("noun", "thing", "other", "flower", "はな", "101", "unit 4", "花"),
              Word("noun", "thing", "other", "picture", "しゃしん", "101", "unit 4", "写真"),
              Word("noun", "thing", "other", "report", "レポート", "101", "unit 4"),
              Word("noun", "thing", "other", "travel", "りょこう", "101", "unit 5", "旅行"),
              Word("noun", "thing", "other", "surfing", "サーフィン", "101", "unit 5"),
              Word("noun", "thing", "other", "souvenir", "おみやげ", "101", "unit 5", "お土産"),
              Word("noun", "thing", "other", "bus", "バス", "101", "unit 5"),
              Word("noun", "thing", "other", "weather", "てんき", "101", "unit 5", "天気"),
              Word("noun", "thing", "other", "homework", "しゅくだい", "101", "unit 5", "宿題"),
              Word("noun", "thing", "other", "size", "サイズ", "101", "unit 5"),
              Word("noun", "thing", "other", "kanji", "かんじ", "101", "unit 6", "漢字"),
              Word("noun", "thing", "other", "textbook", "きょうかしょ", "101", "unit 6", "教科書"),
              Word("noun", "thing", "other", "page", "ページ", "101", "unit 6"),
              Word("noun", "thing", "other", "next", "つぎ", "101", "unit 6", "次"),
              Word("noun", "thing", "other", "money", "おかね", "101", "unit 6", "お金"),
              Word("noun", "thing", "other", "baggage", "にもつ", "101", "unit 6", "荷物"),
              Word("noun", "thing", "other", "personal computer", "パソコン", "101", "unit 6"),
              Word("noun", "thing", "other", "shower", "シャワー", "101", "unit 6"),
              Word("noun", "thing", "other", "air conditioner", "エアコン", "101", "unit 6"),
              Word("noun", "thing", "other", "electricity", "でんき", "101", "unit 6", "電気"),
              Word("noun", "thing", "other", "window", "まど", "101", "unit 6", "窓"),
              Word("noun", "thing", "other", "train", "でんしゃ", "101", "unit 6", "電車"),
              Word("noun", "thing", "other", "test", "テスト", "101　", "unit 5"),
              Word("noun", "thing", "other", "japanese language", "にほんご", "101", "unit 1", "日本語"),
              Word("noun", "thing", "other", "company", "かいしゃ", "102", "unit 7", "会社"),
              Word("noun", "thing", "other", "hair", "かみ", "102", "unit 7", "髪"),
              Word("noun", "thing", "other", "mouth", "くち", "102", "unit 7", "口"),
              Word("noun", "thing", "other", "eye", "め", "102", "unit 7", "目"),
              Word("noun", "thing", "other", "glasses", "めがね", "102", "unit 7", "眼鏡"),
              Word("noun", "thing", "other", "song", "うた", "102", "unit 7", "歌"),
              Word("noun", "thing", "other", "club activity", "サークル", "102", "unit 7"),
              Word("noun", "thing", "other", "car", "くるま", "102", "unit 7", "車"),
              Word("noun", "thing", "other", "sunny weather", "はれ", "102", "unit 8", "晴れ"),
              Word("noun", "thing", "other", "rain", "あめ", "102", "unit 8", "雨"),
              Word("noun", "thing", "other", "cloudy weather", "くもり", "102", "unit 8", "曇り"),
              Word("noun", "thing", "other", "snow", "ゆき", "102", "unit 8", "雪"),
              Word("noun", "thing", "other", "weather forecast", "てんきよほう", "102", "unit 8", "天気予報"),
              Word("noun", "thing", "other", "temperature (weather)", "きおん", "102", "unit 8", "気温"),
              Word("noun", "thing", "other", "something", "なにか", "102", "unit 8", "何か"),
              Word("noun", "thing", "other", "word", "たんご", "102", "unit 9", "単語"),
              Word("noun", "thing", "other", "essay", "さくぶん", "102", "unit 9", "作文"),
              Word("noun", "thing", "other", "exam", "しけん", "102", "unit 9", "試験"),
              Word("noun", "thing", "other", "letter", "てがみ", "102", "unit 9", "手紙"),
              Word("noun", "thing", "other", "e-mail", "メール", "102", "unit 9"),
              Word("noun", "thing", "other", "guitar", "ギター", "102", "unit 9"),
              Word("noun", "thing", "other", "piano", "ピアノ", "102", "unit 9"),
              Word("noun", "thing", "other", "ticket", "チケット", "102", "unit 9"),
              Word("noun", "thing", "other", "ski", "スキー", "102", "unit 9"),
              Word("noun", "thing", "other", "illness", "びょうき", "102", "unit 9", "病気"),
              Word("noun", "thing", "other", "medicine", "くすり", "102", "unit 9", "薬"),
              Word("noun", "thing", "other", "color", "いろ", "102", "unit 9", "色"),
              Word("noun", "thing", "other", "face", "かお", "102", "unit 10", "顔"),
              Word("noun", "thing", "other", "bullet train", "しんかんせん", "102", "unit 10", "新幹線"),
              Word("noun", "thing", "other", "ship", "ふね", "102", "unit 10", "船"),
              Word("noun", "thing", "other", "airplane", "ひこうき", "102", "unit 10", "飛行機"),
              Word("noun", "thing", "other", "reservation", "よやく", "102", "unit 10", "予約"),
              Word("noun", "thing", "other", "tour", "ツアー", "102", "unit 10"),
              Word("noun", "thing", "other", "life", "せいかつ", "102", "unit 10", "生活"),
              Word("noun", "thing", "other", "dream", "ゆめ", "102", "unit 11", "夢"),
              Word("noun", "thing", "other", "class", "じゅぎょう", "102", "unit 11", "授業"),
              Word("noun", "thing", "other", "fishing", "つり", "102", "unit 11"),
              Word("noun", "thing", "other", "drive", "ドライブ", "102", "unit 11"),
              Word("noun", "thing", "other", "stomach", "おなか", "102", "unit 12"),
              Word("noun", "thing", "other", "leg/foot", "あし", "102", "unit 12", "足"),
              Word("noun", "thing", "other", "throat", "のど", "102", "unit 12", "喉"),
              Word("noun", "thing", "other", "tooth", "は", "102", "unit 12", "歯"),
              Word("noun", "thing", "other", "influenza", "インフルエンザ", "102", "unit 12"),
              Word("noun", "thing", "other", "cold", "かぜ", "102", "unit 12", "風邪"),
              Word("noun", "thing", "other", "cough", "せき", "102", "unit 12"),
              Word("noun", "thing", "other", "hangover", "ふつかよい", "102", "unit 12", "二日酔い"),
              Word("noun", "thing", "other", "homesickness", "ホームシッカ", "102", "unit 12"),
              Word("noun", "thing", "other", "allergy", "アレルギー", "102", "unit 12"),
              Word("noun", "thing", "other", "thing (an object)", "もの", "102", "unit 12", "物"),
              Word("noun", "thing", "other", "business (to take  care of)", "ようじ", "102", "unit 12", "用事"),
              Word("noun", "thing", "other", "grade", "せいせき", "102", "unit 12", "載積"),
              Word("noun", "thing", "other", "meaning", "いみ", "102", "unit 12", "意味"),
              Word("noun", "thing", "other", "present (gift)", "プレゼント", "102", "unit 12"),
              Word("noun", "thing", "other", "ticket (train)", "きっぷ", "102", "unit 12", "切符"),
              Word("noun", "thing", "other", "fee", "だい", "102", "unit 12", "代"),
              Word("noun", "thing", "other", "pencil", "えんぴつ", "101", "bonus 1"),
              Word("noun", "thing", "other", "eraser", "けしゴム", "101", "bonus 1"),
              Word("noun", "thing", "other", "dictionary", "じしょ", "101", "bonus 1"),
              Word("noun", "thing", "other", "door", "ドア", "101", "bonus 1"),
              Word("noun", "thing", "other", "curtain", "カーテン", "101", "bonus 1"),
              Word("noun", "thing", "other", "blackboard", "こくばん", "101", "bonus 1"),
              Word("noun", "thing", "other", "straw mats", "たたみ", "101", "bonus 1", "畳"),
              Word("noun", "thing", "other", "sliding door", "じょうじ", "101", "bonus 1", "障子"),
              Word("noun", "thing", "other", "entrance-way (home)", "げんかん", "101", "bonus 1", "玄関"),
              Word("noun", "thing", "other", "graduate school", "だいがくいん", "101", "bonus 1", "大学院"),
              Word("noun", "thing", "other", "junior college", "たんだい", "101", "bonus 1", "短大"),
              Word("noun", "thing", "other", "junior high school", "ちゅうがく", "101", "bonus 1", "中学"),
              Word("noun", "thing", "other", "elementary school", "しょうがっこう", "101", "bonus 1", "小学校"),
              Word("noun", "thing", "other", "nursery school", "ほいくえん", "101", "bonus 1", "保育園"),
              Word("noun", "thing", "other", "kindergarten", "ようちえん", "101", "bonus 1", "幼稚園"),
              Word("noun", "thing", "other", "compulsory education", "ぎむきょういく", "101", "bonus 1", "義務教育"),
              Word("noun", "thing", "other", "eyebrow", "まゆげ", "101", "bonus 1", "眉毛"),
              Word("noun", "thing", "other", "ear", "みみ", "101", "bonus 1", "耳"),
              Word("noun", "thing", "other", "hand", "て", "101", "bonus 1", "手"),
              Word("noun", "thing", "other", "neck", "くび", "101", "bonus 1", "首"),
              Word("noun", "thing", "other", "finger", "ゆび", "101", "bonus 1", "指"),
              Word("noun", "thing", "other", "nose", "はな", "101", "bonus 1", "鼻"),
              Word("noun", "thing", "other", "shoulders", "かた", "101", "bonus 1", "肩"),
              Word("noun", "thing", "other", "chest", "むね", "101", "bonus 1", "胸"),
              Word("noun", "thing", "other", "butt", "おしり", "101", "bonus 1", "お尻"),
              Word("noun", "thing", "other", "back (body part)", "せなか", "101", "bonus 1", "背中"),
              Word("noun", "thing", "other", "head", "あたま", "101", "bonus 1", "頭"),
              Word("noun", "thing", "other", "green", "みどり", "101", "bonus 1", "緑"),
              Word("noun", "thing", "other", "navy blue", "こんいろ", "101", "bonus 1", "紺色"),
              Word("noun", "thing", "other", "light blue", "みずいろ", "101", "bonus 1", "水色"),
              Word("noun", "thing", "other", "silver (color)", "ぎんいろ", "101", "bonus 1", "銀色"),
              Word("noun", "thing", "other", "orange (color)", "オレンジ", "101", "bonus 1"),
              Word("noun", "thing", "other", "purple", "むらさき", "101", "bonus 1", "紫"),
              Word("noun", "thing", "other", "gray", "はいいろ", "101", "bonus 1", "灰色"),
              Word("noun", "thing", "other", "gold (color)", "きんいろ", "101", "bonus 1", "金色"),
              Word("noun", "thing", "other", "pink", "ピンク", "101", "bonus 1"),
              Word("noun", "thing", "other", "beige", "ベージュ", "101", "bonus 1"),
              Word("noun", "thing", "other", "local (train)", "ふつう", "101", "bonus 1", "普通"),
              Word("noun", "thing", "other", "express (train)", "きゅうこう", "101", "bonus 1", "急行"),
              Word("noun", "thing", "other", "super express (train)", "とっきゅう", "101", "bonus 1", "特急"),
              Word("noun", "thing", "other", "boarding ticket", "じょうしゃけん", "101", "bonus 1", "乗車券"),
              Word("noun", "thing", "other", "commuter's pass", "ていきけん", "101", "bonus 1", "定期券"),
              Word("noun", "thing", "other", "student discount", "がくわり", "101", "bonus 1", "学割"),
              Word("noun", "thing", "other", "reserved seat", "していせき", "101", "bonus 1", "指定席"),
              Word("noun", "thing", "other", "general admission seat", "じゆうせき", "101", "bonus 1", "自由席"),
              Word("noun", "thing", "other", "round trip", "おうふく", "101", "bonus 1", "往復"),
              Word("noun", "thing", "other", "one way", "かたみち", "101", "bonus 1", "片道"),
              Word("noun", "thing", "other", "transfer (train)", "のりかえ", "101", "bonus 1", "乗り換え"),
              Word("noun", "thing", "other", "last train", "しゅうでん", "101", "bonus 1", "終電"),
              Word("noun", "thing", "other", "deadline", "しめきり", "101", "bonus 1"),
              Word("noun", "thing", "other", "exercise (in class)", "れんしゅう", "101", "bonus 1", "練習"),
              Word("noun", "thing", "other", "pronunciation", "はつおん", "101", "bonus 1", "発音"),
              Word("noun", "thing", "other", "grammar", "ぶんぽう", "101", "bonus 1", "文法"),
              Word("noun", "thing", "other", "question", "しつもん", "101", "bonus 1", "質問"),
              Word("noun", "thing", "other", "answer", "こたえ", "101", "bonus 1", "答"),
              Word("noun", "thing", "other", "dialect", "ほうげん", "101", "bonus 1", "方言"),
              Word("noun", "thing", "other", "common language", "きょうつうご", "101", "bonus 1", "共通語"),
              Word("noun", "thing", "other", "example", "れい", "101", "bonus 1", "例"),
              Word("noun", "thing", "other", "antibiotic", "こうせいぶっしつ", "101", "bonus 1", "抗生物質"),
              Word("noun", "thing", "other", "operation", "しゅじゅつ", "101", "bonus 1", "手術"),
              Word("noun", "thing", "other", "injection", "ちゅうしゃ", "101", "bonus 1", "注射"),
              Word("noun", "thing", "other", "thermometer", "たいおんけい", "101", "bonus 1", "体温計"),

              Word("pronoun", "", "", "i", "わたし", "101", "unit 1", "私"),
              Word("pronoun", "", "", "i (men)", "ぼく", "101", "unit 5", "僕"),
              Word("pronoun", "", "", "you", "あなた", "101", "unit 4"),

              Word("title", "", "", "Mr./Ms.", "さん", "101", "unit 1"),

              Word("adjective", "i", "", "delicious", "おいしい", "101", "unit 2"),
              Word("adjective", "i", "", "expensive", "たかい", "101", "unit 2", "高い"),
              Word("adjective", "i", "", "early", "はやい", "101", "unit 3", "早い"),
              Word("adjective", "i", "", "new", "あたらしい", "101", "unit 5", "新しい"),
              Word("adjective", "i", "", "old", "ふるい", "101", "unit 5", "古い"),
              Word("adjective", "i", "", "hot (thing)", "あつい", "101", "unit 5", "暑い"),
              Word("adjective", "i", "", "hot (weather)", "あつい", "101", "unit 5", "熱い"),
              Word("adjective", "i", "", "cold", "さむい", "101", "unit 5", "寒い"),
              Word("adjective", "i", "", "busy", "いそがしい", "101", "unit 5", "忙しい"),
              Word("adjective", "i", "", "large", "おおきい", "101", "unit 5", "大きい"),
              Word("adjective", "i", "", "small", "ちいさい", "101", "unit 5", "小さい"),
              Word("adjective", "i", "", "interesting", "おもしろい", "101", "unit 5", "面白い"),
              Word("adjective", "i", "", "boring", "つまらない", "101", "unit 5"),
              Word("adjective", "i", "", "easy", "やさしい", "101", "unit 5"),
              Word("adjective", "i", "", "difficult", "むずかしい", "101", "unit 5", "難しい"),
              Word("adjective", "i", "", "frightening", "こわい", "101", "unit 5", "怖い"),
              Word("adjective", "i", "", "fun", "たのしい", "101", "unit 5", "楽しい"),
              Word("adjective", "i", "", "cheap", "やすい", "101", "unit 5", "安い"),
              Word("adjective", "i", "", "long", "ながい", "102", "unit 7", "長い"),
              Word("adjective", "i", "", "short (length)", "みじかい", "102", "unit 7", "短い"),
              Word("adjective", "i", "", "fast", "はやい", "102", "unit 7", "速い"),
              Word("adjective", "i", "", "tall", "せがたかい", "102", "unit 7", "背が高い"),
              Word("adjective", "i", "", "short (stature)", "せがひくい", "102", "unit 7", "背が低い"),
              Word("adjective", "i", "", "cute", "かわいい", "102", "unit 7"),
              Word("adjective", "i", "", "blue", "あおい", "102", "unit 9", "青い"),
              Word("adjective", "i", "", "red", "あかい", "102", "unit 9", "赤い"),
              Word("adjective", "i", "", "black", "くろい", "102", "unit 9", "黒い"),
              Word("adjective", "i", "", "white", "しろい", "102", "unit 9", "白い"),
              Word("adjective", "i", "", "lonely", "さびしい", "102", "unit 9", "寂しい"),
              Word("adjective", "i", "", "young", "わかい", "102", "unit 9", "若い"),
              Word("adjective", "i", "", "warm", "あたたかい", "102", "unit 10", "暖かい"),
              Word("adjective", "i", "", "cool (weather)", "すずしい", "102", "unit 10", "涼しい"),
              Word("adjective", "i", "", "cold (things)", "つめたい", "102", "unit 10", "冷たい"),
              Word("adjective", "i", "", "slow/late", "おそい", "102", "unit 10", "遅い"),
              Word("adjective", "i", "", "sleepy", "ねむい", "102", "unit 10", "眠い"),
              Word("adjective", "i", "", "narrow/not spacious", "せまい", "102", "unit 12", "狭い"),
              Word("adjective", "i", "", "wide/spacious", "ひろい", "102", "unit 12", "広い"),
              Word("adjective", "i", "", "bad", "わるい", "102", "unit 12", "悪い"),
              Word("adjective", "i", "", "hurt/painful", "いたい", "102", "unit 12", "痛い"),
              Word("adjective", "i", "", "sweet", "あまい", "102", "unit 12", "甘い"),
              Word("adjective", "i", "", "many", "おおい", "102", "unit 12", "多い"),
              Word("adjective", "i", "", "yellow", "きいろい", "102", "bonus 1", "黄色い"),
              Word("adjective", "i", "", "brown", "ちゃいろい", "102", "bonus 1", "茶色い"),
              Word("adjective", "na", "", "like", "すきな", "101", "unit 5", "好きな"),
              Word("adjective", "na", "", "dislike", "きらいな", "101", "unit 5", "嫌いな"),
              Word("adjective", "na", "", "love", "だいすきな", "101", "unit 5", "大好きな"),
              Word("adjective", "na", "", "hate", "だいきらいな", "101", "unit 5", "大嫌いな"),
              Word("adjective", "na", "", "beautiful", "きれいな", "101", "unit 5"),
              Word("adjective", "na", "", "healthy", "げんきな", "101", "unit 5", "元気な"),
              Word("adjective", "na", "", "quiet", "しずかな", "101", "unit 5", "静かな"),
              Word("adjective", "na", "", "lively", "にぎやかな", "101", "unit 5"),
              Word("adjective", "na", "", "not busy", "ひまな", "101", "unit 5", "暇な"),
              Word("adjective", "na", "", "tough (situation)", "たいへんな", "101", "unit 6", "大変な"),
              Word("adjective", "na", "", "kind", "しんせつな", "102", "unit 7", "親切な"),
              Word("adjective", "na", "", "convenient", "べんりな", "102", "unit 7", "便利な"),
              Word("adjective", "na", "", "good at", "じょうずな", "102", "unit 8", "上手な"),
              Word("adjective", "na", "", "poor at", "へたな", "102", "unit 8", "下手な"),
              Word("adjective", "na", "", "famous", "ゆうめいな", "102", "unit 8", "有名な"),
              Word("adjective", "na", "", "mean-spirited", "いじわるな", "102", "unit 9", "意地悪な"),
              Word("adjective", "na", "", "easy/simple", "かんたんな", "102", "unit 10", "簡単な"),
              Word("adjective", "na", "", "nice", "すてきな", "102", "unit 12", "素敵な"),
              Word("adjective", "irregular", "", "good", "いい", "101", "unit 3"),
              Word("adjective", "irregular", "", "good-looking", "かっこいい", "101", "unit 5"),
              Word("adjective", "irregular", "", "smart", "あたまがいい", "102", "unit 7", "頭がいい"),

              Word("adverb", "", "", "not much", "あまり", "101", "unit 3"),
              Word("adverb", "", "", "not at all", "ぜんぜん", "101", "unit 3", "全然"),
              Word("adverb", "", "", "usually", "たいてい", "101", "unit 3"),
              Word("adverb", "", "", "a little", "ちょっと", "101", "unit 3"),
              Word("adverb", "", "", "sometimes", "ときどき", "101", "unit 3", "時々"),
              Word("adverb", "", "", "often", "よく", "101", "unit 3"),
              Word("adverb", "", "", "about", "ぐらい", "101", "unit 4"),
              Word("adverb", "", "", "together", "いっしょに", "101", "unit 5", "一緒に"),
              Word("adverb", "", "", "extremely", "すごく", "101", "unit 5"),
              Word("adverb", "", "", "very", "とても", "101", "unit 5"),
              Word("adverb", "", "", "leisurely", "ゆっくり", "101", "unit 6"),
              Word("adverb", "", "", "always", "いつも", "102", "unit 8"),
              Word("adverb", "", "", "(do something) late", "おそく", "102", "unit 8", "遅く"),
              Word("adverb", "", "", "(do something) early", "はやく", "102", "unit 10", "早く"),
              Word("adverb", "", "", "(do something) fast", "はやく", "102", "unit 10", "速く"),
              Word("adverb", "", "", "many", "たくさん", "101", "unit 4"),
              Word("adverb", "", "", "alone", "ひとりで", "101", "unit 4", "一人で"),

              Word("preposition", "time", "", "now", "いま", "101", "unit 1", "今"),
              Word("preposition", "time", "", "later on", "あとで", "101", "unit 6", "後で"),
              Word("preposition", "time", "", "right away", "すぐ", "101", "unit 6"),
              Word("preposition", "time", "", "not ... yet", "まだ", "102", "unit 8"),
              Word("preposition", "time", "", "already", "もう", "102", "unit 9"),
              Word("preposition", "location", "", "this", "この", "101", "unit 2"),
              Word("preposition", "location", "", "that", "その", "101", "unit 2"),
              Word("preposition", "location", "", "that over there", "あの", "101", "unit 2"),
              Word("preposition", "location", "", "here", "ここ", "101", "unit 2"),
              Word("preposition", "location", "", "there", "そこ", "101", "unit 2"),
              Word("preposition", "location", "", "over there", "あそこ", "101", "unit 2"),
              Word("preposition", "location", "", "right", "みぎ", "101", "unit 4", "右"),
              Word("preposition", "location", "", "left", "ひだり", "101", "unit 4", "左"),
              Word("preposition", "location", "", "front", "まえ", "101", "unit 4", "前"),
              Word("preposition", "location", "", "back (of something)", "うしろ", "101", "unit 4", "後ろ"),
              Word("preposition", "location", "", "inside", "なか", "101", "unit 4", "中"),
              Word("preposition", "location", "", "on", "うえ", "101", "unit 4", "上"),
              Word("preposition", "location", "", "under", "した", "101", "unit 4", "下"),
              Word("preposition", "location", "", "near", "ちかく", "101", "unit 4", "近く"),
              Word("preposition", "location", "", "next", "となり", "101", "unit 4", "隣"),
              Word("preposition", "location", "", "between", "あいだ", "101", "unit 4", "間"),
              Word("preposition", "location", "", "from...", "から", "102", "unit 9"),
              Word("preposition", "location", "", "to (a place/a time)", "まで", "102", "unit 9"),
              Word("preposition", "location", "", "coming from", "しゅっしん", "102", "unit 11", "出身"),
              Word("preposition", "location", "", "north", "きた", "102", "bonus 1", "北"),
              Word("preposition", "location", "", "south", "みなみ", "102", "bonus 1", "南"),
              Word("preposition", "location", "", "east", "ひがし", "102", "bonus 1", "東"),
              Word("preposition", "location", "", "west", "にし", "102", "bonus 1", "西"),
              Word("preposition", "time", "", "and then", "それから", "101", "unit 4"),
              Word("preposition", "time", "", "and then", "そして", "102", "unit 11"),
              Word("preposition", "time", "", "after (an event)", "あと", "102", "unit 11", "後"),
              Word("preposition", "time", "", "as much as possible", "できるだけ", "102", "unit 12"),
              Word("preposition", "time", "", "very soon", "もうすぐ", "102", "unit 12"),
              Word("preposition", "time", "", "for the first time", "はじめて", "102", "unit 12", "初めて"),
              Word("preposition", "time", "", "for two or three more days", "にさんにち", "102", "unit 12", "二三日"),

              Word("time", "", "", "half past", "はん", "101", "unit 1"),
              Word("time", "", "", "p.m.", "ごご", "101", "unit 1"),
              Word("time", "", "", "a.m.", "ごぜん", "101", "unit 1"),
              Word("time", "", "", "at about", "ごろ", "101", "unit 3"),
              Word("time", "", "", "at the time of", "とき", "101", "unit 4", "時"),

              Word("question", "", "", "what", "なに", "101", "unit 1", "何"),
              Word("question", "", "", "which one", "どれ", "101", "unit 2"),
              Word("question", "", "", "which", "どの", "101", "unit 2"),
              Word("question", "", "", "where", "どこ", "101", "unit 2"),
              Word("question", "", "", "who", "だれ", "101", "unit 2"),
              Word("question", "", "", "why", "どうして", "101", "unit 4"),
              Word("question", "", "", "when", "いつ", "101", "unit 3"),
              Word("question", "", "", "how much", "いくら", "101", "unit 2"),
              Word("question", "", "", "what kind of", "どんな", "101", "unit 5"),
              Word("question", "", "", "really", "ほんとうですか", "101", "unit 6", "本当ですか"),
              Word("question", "", "", "how", "どう", "102", "unit 8"),
              Word("question", "", "", "which", "どっち", "102", "unit 10"),
              Word("question", "", "", "how/by what means", "どうやって", "102", "unit 10"),
              Word("question", "", "", "how much/long", "どのぐらい", "102", "unit 10"),

              Word("verb", "u", "き", "to go", "いく", "101", "unit 3", "行く"),
              Word("verb", "u", "り", "to go back", "かえる", "101", "unit 3", "帰る"),
              Word("verb", "u", "き", "to listen", "きく", "101", "unit 3", "聞く"),
              Word("verb", "u", "み", "to drink", "のむ", "101", "unit 3", "飲む"),
              Word("verb", "u", "し", "to speak", "はなす", "101", "unit 3", "話す"),
              Word("verb", "u", "み", "to read", "よむ", "101", "unit 3", "読む"),
              Word("verb", "u", "い", "to meet", "あう", "101", "unit 4", "会う"),
              Word("verb", "u", "り", "is (non-living thing)", "ある", "101", "unit 4"),
              Word("verb", "u", "い", "to buy", "かう", "101", "unit 4", "買う"),
              Word("verb", "u", "き", "to write", "かく", "101", "unit 4", "書く"),
              Word("verb", "u", "り", "to take a picture", "とる", "101", "unit 4", "撮る"),
              Word("verb", "u", "ち", "to wait", "まつ", "101", "unit 4", "待つ"),
              Word("verb", "u", "ぎ", "to swim", "およぐ", "101", "unit 5", "泳ぐ"),
              Word("verb", "u", "き", "to ask", "きく", "101", "unit 5", "聞く"),
              Word("verb", "u", "り", "to ride", "のる", "101", "unit 5", "乗る"),
              Word("verb", "u", "り", "to perform", "やる", "101", "unit 5"),
              Word("verb", "u", "り", "to understand", "わかる", "101", "unit 4"),
              Word("verb", "u", "び", "to play", "あそぶ", "101", "unit 6", "遊ぶ"),
              Word("verb", "u", "ぎ", "to hurry", "いそぐ", "101", "unit 6", "急ぐ"),
              Word("verb", "u", "し", "to return", "かえす", "101", "unit 6", "返す"),
              Word("verb", "u", "し", "to turn off", "けす", "101", "unit 6", "消す"),
              Word("verb", "u", "に", "to die", "しぬ", "101", "unit 6", "死ぬ"),
              Word("verb", "u", "り", "to sit down", "すわる", "101", "unit 6", "座る"),
              Word("verb", "u", "ち", "to stand up", "たつ", "101", "unit 6", "立つ"),
              Word("verb", "u", "い", "to smoke", "たばこをすう", "101", "unit 6", "たばこを吸う"),
              Word("verb", "u", "い", "to use", "つかう", "101", "unit 6", "使う"),
              Word("verb", "u", "い", "to help", "てつだう", "101", "unit 6", "手伝う"),
              Word("verb", "u", "り", "to enter", "はいる", "101", "unit 6", "入る"),
              Word("verb", "u", "ち", "to carry", "もつ", "101", "unit 6", "持つ"),
              Word("verb", "u", "み", "to rest", "やすむ", "101", "unit 6", "休む"),
              Word("verb", "u", "い", "to sing", "うたう", "102", "unit 7", "歌う"),
              Word("verb", "u", "り", "to put on (a hat)", "かぶる", "102", "unit 7"),
              Word("verb", "u", "き", "to put on (items below your waist)", "はく", "102", "unit 7"),
              Word("verb", "u", "り", "to get to know", "しる", "102", "unit 7", "知る"),
              Word("verb", "u", "み", "to live", "すむ", "102", "unit 7", "住む"),
              Word("verb", "u", "き", "to work", "はたらく", "102", "unit 7", "働く"),
              Word("verb", "u", "り", "to gain weight", "ふとる", "102", "unit 7", "太る"),
              Word("verb", "u", "い", "to wash", "あらう", "102", "unit 8", "洗う"),
              Word("verb", "u", "い", "to say", "いう", "102", "unit 8", "言う"),
              Word("verb", "u", "り", "to need", "いる", "102", "unit 8"),
              Word("verb", "u", "り", "to be late", "おすくなる", "102", "unit 8", "遅くなる"),
              Word("verb", "u", "り", "to take a bath", "おふろにはいる", "102", "unit 8", "お風呂に入る"),
              Word("verb", "u", "い", "to think", "おもう", "102", "unit 8", "思う"),
              Word("verb", "u", "り", "to cut", "きる", "102", "unit 8", "切る"),
              Word("verb", "u", "り", "to make", "つくる", "102", "unit 8", "作る"),
              Word("verb", "u", "り", "to fall (rain/snow)", "ふる", "102", "unit 8", "降る"),
              Word("verb", "u", "き", "to take (a thing)", "もっていく", "102", "unit 8", "持っていく"),
              Word("verb", "u", "り", "to dance", "おどる", "102", "unit 9", "踊る"),
              Word("verb", "u", "り", "to end (something ends)", "おわる", "102", "unit 9", "終わる"),
              Word("verb", "u", "み", "to take medicine", "くすりをのむ", "102", "unit 9", "薬を飲む"),
              Word("verb", "u", "り", "to be popular", "にんきがある", "102", "unit 9", "人気がある"),
              Word("verb", "u", "り", "to begin (something begins)", "はじまる", "102", "unit 9", "始まる"),
              Word("verb", "u", "き", "to play (an instrument)", "ひく", "102", "unit 9", "弾く"),
              Word("verb", "u", "い", "to get (from somebody)", "もらう", "102", "unit 9"),
              Word("verb", "u", "り", "to take (time/money)", "かかる", "102", "unit 10"),
              Word("verb", "u", "り", "to stay (at hotel, etc.)", "とまる", "102", "unit 10", "泊まる"),
              Word("verb", "u", "り", "to become", "なる", "102", "unit 10"),
              Word("verb", "u", "き", "to tell a lie", "うそをつく", "102", "unit 11"),
              Word("verb", "u", "き", "to become hungry", "おなかがすく", "102", "unit 11"),
              Word("verb", "u", "い", "to own (a pet)", "かう", "102", "unit 11", "飼う"),
              Word("verb", "u", "り", "to cut (class)", "サボる", "102", "unit 11"),
              Word("verb", "u", "り", "to take/get (class/grade)", "とる", "102", "unit 11", "取る"),
              Word("verb", "u", "い", "to learn", "ならう", "102", "unit 11", "習う"),
              Word("verb", "u", "り", "to climb", "のぼる", "102", "unit 11", "登る"),
              Word("verb", "u", "り", "to run", "はしる", "102", "unit 11", "走る"),
              Word("verb", "u", "き", "to walk", "おるく", "102", "unit 12", "歩く"),
              Word("verb", "u", "き", "to catch a cold", "かぜをひく", "102", "unit 12", "風邪をひく"),
              Word("verb", "u", "り", "to have a fever", "ねつがある", "102", "unit 12", "熱がある"),
              Word("verb", "u", "き", "to become thirsty", "のどがかわく", "102", "unit 12", "喉が渇く"),
              Word("verb", "u", "い", "to pay", "はらう", "102", "unit 12", "払う"),
              Word("verb", "u", "し", "to lose", "なくす", "102", "unit 12"),
              Word("verb", "u", "り", "to be interested", "きょうみがある", "102", "unit 12", "興味がある"),
              Word("verb", "ru", "", "to get up", "おきる", "101", "unit 3", "起きる"),
              Word("verb", "ru", "", "to eat", "たべる", "101", "unit 3", "食べる"),
              Word("verb", "ru", "", "to sleep", "ねる", "101", "unit 3", "寝る"),
              Word("verb", "ru", "", "to see", "みる", "101", "unit 3", "見る"),
              Word("verb", "ru", "", "is (living thing)", "いる", "101", "unit 4"),
              Word("verb", "ru", "", "to open", "あける", "101", "unit 6", "開ける"),
              Word("verb", "ru", "", "to close", "しめる", "101", "unit 6", "閉める"),
              Word("verb", "ru", "", "to teach", "おしえる", "101", "unit 6", "教える"),
              Word("verb", "ru", "", "to forget", "わすれる", "101", "unit 6", "忘れる"),
              Word("verb", "ru", "", "to get off", "おりる", "101", "unit 6", "降りる"),
              Word("verb", "ru", "", "to borrow", "かりる", "101", "unit 6", "借りる"),
              Word("verb", "ru", "", "to take a shower", "シャワーをあびる", "101", "unit 6", "シャワーを浴びる"),
              Word("verb", "ru", "", "to turn on", "つける", "101", "unit 6"),
              Word("verb", "ru", "", "to go out", "でかける", "101", "unit 5", "出かける"),
              Word("verb", "ru", "", "to put on (glasses)", "かける", "102", "unit 7"),
              Word("verb", "ru", "", "to put on (clothes above waist)", "きる", "102", "unit 7", "着る"),
              Word("verb", "ru", "", "to lose weight", "やせる", "102", "unit 7"),
              Word("verb", "ru", "", "to throw away", "すてる", "102", "unit 8", "捨てる"),
              Word("verb", "ru", "", "to begin", "はじめる", "102", "unit 8", "始める"),
              Word("verb", "ru", "", "to memorize", "おぼえる", "102", "unit 9", "覚える"),
              Word("verb", "ru", "", "to attend/to exit", "でる", "102", "unit 9", "出る"),
              Word("verb", "ru", "", "to decide", "きめる", "102", "unit 10", "決める"),
              Word("verb", "ru", "", "to get tired", "つかれる", "102", "unit 11", "疲れる"),
              Word("verb", "ru", "", "to quit", "やめる", "102", "unit 11"),
              Word("verb", "ru", "", "to cough", "せきがでる", "102", "unit 12", "せきが出る"),
              Word("verb", "ru", "", "to break up", "わかれる", "102", "unit 12", "別れる"),
              Word("verb", "irregular", "くる", "to come", "くる", "101", "unit 3", "来る"),
              Word("verb", "irregular", "する", "to do", "する", "101", "unit 3"),
              Word("verb", "irregular", "する", "to study", "べんきょうする", "101", "unit 3", "勉強する"),
              Word("verb", "irregular", "する", "to call", "でんわする", "101", "unit 6", "電話する"),
              Word("verb", "irregular", "くる", "to bring (person)", "つれてくる", "101", "unit 6", "連れてくる"),
              Word("verb", "irregular", "くる", "to bring (thing)", "もってくる", "101", "unit 6", "持ってくる"),
              Word("verb", "irregular", "する", "to get married", "けっこんする", "102", "unit 7", "結婚する"),
              Word("verb", "irregular", "する", "to drive", "うんてんする", "102", "unit 8", "運転する"),
              Word("verb", "irregular", "する", "to do laundry", "せんたくする", "102", "unit 8", "洗濯する"),
              Word("verb", "irregular", "する", "to clean", "そうじする", "102", "unit 8", "掃除する"),
              Word("verb", "irregular", "する", "to cook", "りょうりする", "102", "unit 8", "料理する"),
              Word("verb", "irregular", "する", "to exercise", "うんどうする", "102", "unit 9", "運動する"),
              Word("verb", "irregular", "する", "to take a walk", "さんぽする", "102", "unit 9", "散歩する"),
              Word("verb", "irregular", "する", "to chill/do nothing", "ごろごろする", "102", "unit 10"),
              Word("verb", "irregular", "する", "to travel", "りょこうする", "102", "unit 10", "旅行する"),
              Word("verb", "irregular", "する", "to practice", "れんしゅうする", "102", "unit 10", "練習する"),
              Word("verb", "irregular", "する", "to have a fight", "けんかする", "102", "unit 11"),
              Word("verb", "irregular", "する", "to introduce", "しょうかいする", "102", "unit 11", "紹介する"),
              Word("verb", "irregular", "する", "to go on a diet", "ダイエットする", "102", "unit 11"),
              Word("verb", "irregular", "する", "to be late (for an appointment)",
                   "ちこくする", "102", "unit 11", "遅刻する"),
              Word("verb", "irregular", "する", "to study abroad", "りゅうがくする", "102", "unit 11", "留学する"),
              Word("verb", "irregular", "する", "to get nervous", "きんちょうする", "102", "unit 12", "緊張する"),
              Word("verb", "irregular", "する", "to worry", "しんぱいする", "102", "unit 12", "心配する"),

              Word("expressions", "", "", "um", "あのう", "101", "unit 1"),
              Word("expressions", "", "", "yes", "はい", "101", "unit 1"),
              Word("expressions", "", "", "yeah", "ええ", "101", "unit 3"),
              Word("expressions", "", "", "yes it is", "そうです", "101", "unit 1"),
              Word("expressions", "", "", "welcome", "いらっしゃいませ", "101", "unit 2"),
              Word("expressions", "", "", "please", "おねがいします", "101", "unit 2"),
              Word("expressions", "", "", "please give me", "ください", "101", "unit 2"),
              Word("expressions", "", "", "in that case", "じゃあ", "101", "unit 2"),
              Word("expressions", "", "", "here it is", "どうぞ", "101", "unit 2"),
              Word("expressions", "", "", "thanks", "どうも", "101", "unit 2"),
              Word("expressions", "", "", "that's right", "そうですね", "101", "unit 3"),
              Word("expressions", "", "", "but", "でも", "101", "unit 3"),
              Word("expressions", "", "", "that would be fine", "けっこうです　", "101", "unit 6", "結構です"),
              Word("expressions", "", "", "so", "だから", "101", "unit 4"),
              Word("expressions", "", "", "im sorry", "ごめんなさい", "101", "unit 4"),
              Word("expressions", "", "", "how about", "どうですか", "101", "unit 3"),
              Word("expressions", "", "", "hello (phone)", "もしもし", "101", "unit 4"),
              Word("expressions", "", "", "don't worry", "だいじょうぶ", "101", "unit 5", "大丈夫"),
              Word("expressions", "", "", "good morning", "おはようございます", "101", "unit 1"),
              Word("expressions", "", "", "good afternoon", "こんにちは", "101", "unit 1"),
              Word("expressions", "", "", "good evening", "こんばんは", "101", "unit 1"),
              Word("expressions", "", "", "goodbye", "さようなら", "101", "unit 1"),
              Word("expressions", "", "", "good night", "おやすみなさい", "101", "unit 1"),
              Word("expressions", "", "", "thank you", "ありがとうございます", "101", "unit 1"),
              Word("expressions", "", "", "excuse me", "すみません", "101", "unit 1"),
              Word("expressions", "", "", "no", "いいえ", "101", "unit 1"),
              Word("expressions", "", "", "i'll go and come back", "いってきます", "101", "unit 1"),
              Word("expressions", "", "", "please go and come back", "いってらっしゃい", "101", "unit 1"),
              Word("expressions", "", "", "i'm home", "ただいま", "101", "unit 1"),
              Word("expressions", "", "", "welcome home", "おかえりなさい", "101", "unit 1"),
              Word("expressions", "", "", "thank you for the meal (before)", "いただきます", "101", "unit 1"),
              Word("expressions", "", "", "thank you for the meal (after)", "ごちそうさまでした", "101", "unit 1"),
              Word("expressions", "", "", "how do you do", "はじめまして", "101", "unit 1"),
              Word("expressions", "", "", "nice to meet you", "よろしくおねがいします", "101", "unit 1"),
              Word("expressions", "", "", "years old", "さい", "101", "unit 1"),
              Word("expressions", "", "", "one year old", "いっさい", "101", "unit 1"),
              Word("expressions", "", "", "eight years old", "はっさい", "101", "unit 1"),
              Word("expressions", "", "", "ten years old", "じゅっさい", "101", "unit 1"),
              Word("expressions", "", "", "twenty years old", "はたち", "101", "unit 1"),
              Word("expressions", "", "", "do you understand", "わかりましたか", "101", "unit 2"),
              Word("expressions", "", "", "i understand", "わかりました", "101", "unit 2"),
              Word("expressions", "", "", "i don't understand", "わかりません", "101", "unit 2"),
              Word("expressions", "", "", "please say it slowly", "ゆっくりいってください", "101", "unit 2"),
              Word("expressions", "", "", "please say it again", "もういちどいってください", "101", "unit 2"),
              Word("expressions", "", "", "please wait for a while", "ちょっとまってください", "101", "unit 2"),
              Word("expressions", "", "", "please listen", "きいてください", "102", "unit 2"),
              Word("expressions", "", "", "but", "が", "102", "unit 7"),
              Word("expressions", "", "", "not ... anything", "なにも", "102", "unit 7", "何も"),
              Word("expressions", "", "", "nothing in particular", "べつに", "102", "unit 7", "別に"),
              Word("expressions", "", "", "of course", "もちろん", "102", "unit 7"),
              Word("expressions", "", "", "if you like", "よかったら", "102", "unit 7"),
              Word("expressions", "", "", "uh-huh", "うん", "102", "unit 8"),
              Word("expressions", "", "", "uh-uh", "ううん", "102", "unit 8"),
              Word("expressions", "", "", "Cheers", "かんぱい", "102", "unit 8", "乾杯"),
              Word("expressions", "", "", "all together", "みんなで", "102", "unit 8"),
              Word("expressions", "", "", "that's too bad", "ざんねんですね", "102", "unit 8", "残念ですね"),
              Word("expressions", "", "", "about/concerning", "について", "102", "unit 8"),
              Word("expressions", "", "", "degrees (temperature)", "ど", "102", "unit 8", "度"),
              Word("expressions", "", "", "I think so", "そう", "102", "unit 9"),
              Word("expressions", "", "", "by all means", "ぜひ", "102", "unit 9", "是非"),
              Word("expressions", "", "", "by the way", "ところで", "102", "unit 9"),
              Word("expressions", "", "", "all", "みんな", "102", "unit 9"),
              Word("expressions", "", "", "best", "いちばん", "102", "unit 10", "一番"),
              Word("expressions", "", "", "on foot", "あるいて", "102", "unit 10", "歩いて"),
              Word("expressions", "", "", "these days", "このごろ", "102", "unit 10"),
              Word("expressions", "", "", "it has been a long time", "ひさしぶり", "102", "unit 11", "久しぶり"),
              Word("expressions", "", "", "okay/so-so", "まあまあ", "102", "unit 11"),
              Word("expressions", "", "", "more", "もっと", "102", "unit 11"),
              Word("expressions", "", "", "just/only", "だけ", "102", "unit 11"),
              Word("expressions", "", "", "points", "てん", "102", "unit 11", "点"),
              Word("expressions", "", "", "get well soon", "おだいじに", "102", "unit 12", "お大事に"),
              Word("expressions", "", "", "don't look well", "げんきがない", "102", "unit 12", "元気がない"),
              Word("expressions", "", "", "probably", "たぶん", "102", "unit 12", "多分"),
              Word("expressions", "", "", "moreover", "それに", "102", "unit 12"),
              Word("expressions", "", "", "same", "おなじ", "102", "unit 12", "同じ"),
              Word("expressions", "", "", "for example", "たとえば", "102", "bonus 1"),
              Word("expressions", "", "", "anything else", "ほかに", "102", "bonus 1"),
              Word("expressions", "", "", "is that so", "そうですか", "101", "unit 1")]

# The following is a list of all the particles the user can study
part_list = [Particle("は", ["marks the topic of the sentence"]),
             Particle("の", ["shows possession or specification between two nouns"]),
             Particle("か", ["makes a sentence a question"]),
             Particle("も", ["can replace particles to mean \"also\" or \"too\""]),
             Particle("ね", ["conveys that the speaker is seeking confirmation in their statement"]),
             Particle("よ", ["conveys that the speaker is confidently informing the listener of something"]),
             Particle("に", ["can mark the destination of a movement verb, but has other uses",
                            "marks the absolute time that an event occurs",
                            "marks the place where the verb happens only when using ある or いる"]),
             Particle("を", ["marks a direct object affected by or relating to a verb"]),
             Particle("で", ["marks the place where the verb happens"]),
             Particle("が", ["identifies the noun that performs the verb"]),
             Particle("へ", ["only marks the destination of a movement verb"]),
             Particle("と", ["groups to nouns together",
                            "is used to show two nouns doing an action together"]),
             Particle("X", ["No particle"])]

# A list of all counters for the counter trainer
counter_list = [Counter("ドル", "dollars", "1", ""),
                Counter("まい", "sheets (flat objects)", "1", "枚"),
                Counter("ど", "degrees", "1", "度"),
                Counter("じかん", "hours", "2", "時間"),
                Counter("ねんかん", "years", "3", "年間"),
                Counter("にん", "people", "13", "人"),
                Counter("えん", "yen", "3", "円"),
                Counter("ふんかん", "minutes", "4", "分間"),
                Counter("ほん", "sticks (long and thin objects)", "5", "本"),
                Counter("はい", "cups", "5", "杯"),
                Counter("ひき", "animals", "5", "匹"),
                Counter("ページ", "(page)", "6", ""),
                Counter("ポンド", "pounds", "6", ""),
                Counter("かげつ", "months", "7", "か月"),
                Counter("か", "(lesson)", "7", "課"),
                Counter("かい", "times", "7", "回"),
                Counter("こ", "small items (small and round)", "7", "個"),
                Counter("かい", "(floor)", "8", "階"),
                Counter("けん", "houses", "8", "軒"),
                Counter("セント", "cents", "9", ""),
                Counter("しゅうかん", "weeks", "9", "週間"),
                Counter("さつ", "books", "9", "冊"),
                Counter("さい", "years of age", "9", "歳"),
                Counter("そく", "shoes", "10", "足"),
                Counter("つう", "letters", "11", "通"),
                Counter("つ", "items (general)", "12", ""),
                Counter("ちょうめ", "(street address)", "11", "丁目")]

# Many global variables are used as the variables are needed in various different windows that run in different
# functions
# current word is the word that the user is being tested on in the vocab trainer
global current
# new button is the button that calls get word, which moves to the next word in the vocab trainer
global new_button
# prompt is a label in the vocab window that gives the user there vocab to practice
global prompt
# feedback is a label that tells the user whether their answer was correct or not
global feedback
# input_box is an entry where the user can enter their response in the vocab trainer
global input_box
# the following are the checkboxes for the word types in the vocab menu
global noun
global pronoun
global title
global adjective
global adverb
global preposition
global time
global question
global verb
global expression
# checkboxes to select what the user wants to study in the character trainer
global katakana
global hiragana
# the number the user is working on
global current_num
# the time the user is given
global current_time
# month and day are strings containing the current date
global month
global day
# answer is a label used to show the user the answer if they request it in the vocab trainer
global answer
global show_button
# enter is the button in the vocab trainer that allows the user to submit their answer
global enter
# current_conj is a string that holds the conjugation type being used at the time
global current_conj
# used to determine whether kanji will be used in practice sessions
global is_kanji
# the label for the progress in the session
global progress
# used to display the progress in a round
global round_total
global round_counter
# label for progress in round
global curr_round
# determines whether session is test or flashcards
global session_type
global session_type_alt
global mod_katakana
global comp_katakana
global rare_katakana
global mod_hiragana
global comp_hiragana
# the main window
global root
global window_width
global window_height
global full_screen
global window_option
global main_frame


def character_menu():
    # This function creates the menu that allows user to customize their character study session
    global katakana
    global hiragana
    global mod_katakana
    global comp_katakana
    global rare_katakana
    global mod_hiragana
    global comp_hiragana
    global root
    global session_type
    global main_frame

    for widget in main_frame.winfo_children():
        widget.destroy()

    hiragana = IntVar()
    mod_hiragana = IntVar()
    comp_hiragana = IntVar()
    katakana = IntVar()
    mod_katakana = IntVar()
    comp_katakana = IntVar()
    rare_katakana = IntVar()
    session_type = StringVar()
    session_type.set("flashcard")

    type_label = Label(main_frame, text="Select the character types you would like to study:", padx=50)
    session_label = Label(main_frame, text="Select which session type you would like:", padx=50)

    katakana_check = Checkbutton(main_frame, text="katakana", variable=katakana)
    mod_katakana_check = Checkbutton(main_frame, text="modified katakana", variable=mod_katakana)
    comp_katakana_check = Checkbutton(main_frame, text="compound katakana", variable=comp_katakana)
    rare_katakana_check = Checkbutton(main_frame, text="rare katakana", variable=rare_katakana)
    hiragana_check = Checkbutton(main_frame, text="hiragana", variable=hiragana)
    mod_hiragana_check = Checkbutton(main_frame, text="modified hiragana", variable=mod_hiragana)
    comp_hiragana_check = Checkbutton(main_frame, text="compound hiragana", variable=comp_hiragana)
    flashcard = Radiobutton(main_frame, text="flashcards", variable=session_type, value="flashcard")
    test_session = Radiobutton(main_frame, text="test", variable=session_type, value="test")

    type_label.grid(row=0, column=0)
    katakana_check.grid(row=1, column=0)
    mod_katakana_check.grid(row=2, column=0)
    comp_katakana_check.grid(row=3, column=0)
    rare_katakana_check.grid(row=4, column=0)
    hiragana_check.grid(row=5, column=0)
    mod_hiragana_check.grid(row=6, column=0)
    comp_hiragana_check.grid(row=7, column=0)
    session_label.grid(row=0, column=1)
    flashcard.grid(row=1, column=1)
    test_session.grid(row=2, column=1)

    session_button = Button(main_frame, text="Create Session", command=create_character_session, pady=10)

    session_button.grid(row=8, column=0, columnspan=1)


def create_character_session():
    # This function creates a session by creating a session list and calling the character session window function
    global main_frame
    global current

    session_list.clear()
    current = 0
    global katakana
    if katakana.get() == 1:
        for i in range(len(char_list)):
            if char_list[i].char_type == "katakana":
                session_list.append(char_list[i])
    if mod_katakana.get() == 1:
        for i in range(len(char_list)):
            if char_list[i].char_type == "mod katakana":
                session_list.append(char_list[i])
    if comp_katakana.get() == 1:
        for i in range(len(char_list)):
            if char_list[i].char_type == "comp katakana":
                session_list.append(char_list[i])
    if rare_katakana.get() == 1:
        for i in range(len(char_list)):
            if char_list[i].char_type == "rare katakana":
                session_list.append(char_list[i])
    global hiragana
    if hiragana.get() == 1:
        for i in range(len(char_list)):
            if char_list[i].char_type == "hiragana":
                session_list.append(char_list[i])
    if mod_hiragana.get() == 1:
        for i in range(len(char_list)):
            if char_list[i].char_type == "mod hiragana":
                session_list.append(char_list[i])
    if comp_hiragana.get() == 1:
        for i in range(len(char_list)):
            if char_list[i].char_type == "comp hiragana":
                session_list.append(char_list[i])

    shuffle_list(session_list)
    character_session_window()


def character_session_window():
    # This function runs the character trainer session
    global main_frame
    global new_button
    global prompt
    global feedback
    global answer
    global show_button
    global enter

    for widget in main_frame.winfo_children():
        widget.destroy()

    new_button = Button(main_frame, text="New Character", command=get_char)
    global input_box
    input_box = Entry(main_frame, font=("Arial", 30))
    enter = Button(main_frame, text="Enter", command=test_char)
    if session_type.get() == "flashcard":
        enter["state"] = DISABLED
    prompt = Label(main_frame, text="Select the new word character to start practicing", font=("Arial", 15))
    feedback = Label(main_frame, text="Press the enter button to test your answer", font=("Arial", 15))
    show_button = Button(main_frame, text="Show Answer", command=show_char)
    answer = Label(main_frame, text="", font=("Arial", 15))
    Button(main_frame, text="main menu", font=("Arial", 15), command=main_menu).grid(row=0, column=3)

    new_button.grid(row=1, column=0)
    input_box.grid(row=0, column=0, columnspan=3)
    enter.grid(row=1, column=2)
    prompt.grid(row=2, column=0, columnspan=3)
    feedback.grid(row=3, column=0, columnspan=3)
    show_button.grid(row=1, column=1)


def get_char():
    # this function gets a character from the session list and stores it in current char
    global current
    global main_frame
    global new_button
    global prompt
    global feedback
    global show_button
    global enter

    counter = len(session_list)
    current = (current + 1) % len(session_list)
    # This loop ensures that users will only receive characters that have not been correctly identified
    # 3 times in a row
    while session_list[current].num_correct > 2 and counter > 0:
        current = (current + 1) % len(session_list)
        counter -= 1
    # if all characters in the session list have been identified correctly 3 times in a row, they are all reset
    if counter == 0:
        for i in range(len(session_list)):
            session_list[i].num_correct = 0
    prompt_text = "Enter the romaji for " + session_list[current].character + ":"
    # A random word is selected from the session list
    prompt.destroy()
    prompt = Label(main_frame, text=prompt_text, font=("Arial", 15))
    prompt.grid(row=2, column=0, columnspan=3)
    # The old prompt is erased and the prompt for the new word is created and displayed
    new_button["state"] = DISABLED
    show_button["state"] = NORMAL
    if session_type.get() == "test":
        enter["state"] = NORMAL
    feedback.destroy()
    # The user is blocked from choosing a new word and the old feedback is removed to keep things running smooth
    if session_type.get() == "flashcard":
        answer.destroy()


def test_char():
    # This function checks whether the correct answer was entered
    global main_frame
    global input_box
    global new_button
    global feedback
    global answer
    global show_button
    global enter

    current_entry = input_box.get()
    if current_entry == session_list[current].romaji:
        session_list[current].num_correct += 1
        if feedback.winfo_exists() == 1:
            feedback.destroy()
        if answer.winfo_exists() == 1:
            answer.destroy()
        feedback = Label(main_frame, text="correct", font=("Arial", 15))
        feedback.grid(row=3, column=0, columnspan=3)
        input_box.delete(0, "end")
        new_button["state"] = NORMAL
        enter["state"] = DISABLED
    else:
        session_list[current].num_correct = 0
        if feedback.winfo_exists() == 1:
            feedback.destroy()
        feedback = Label(main_frame, text="incorrect", font=("Arial", 15))
        feedback.grid(row=3, column=0, columnspan=3)


def show_char():
    # This function displays the current word
    global main_frame
    global current
    global answer
    global show_button

    session_list[current].num_correct = 0
    answer = Label(main_frame, text=session_list[current].romaji, font=("Arial", 15))
    answer.grid(row=4, column=0, columnspan=3)
    show_button["state"] = DISABLED
    if session_type.get() == "flashcard":
        new_button["state"] = NORMAL


def character_w_menu():
    # This function creates the menu that allows user to customize their character writing session
    global katakana
    global hiragana
    global mod_katakana
    global comp_katakana
    global rare_katakana
    global mod_hiragana
    global comp_hiragana
    global main_frame

    for widget in main_frame.winfo_children():
        widget.destroy()

    hiragana = IntVar()
    mod_hiragana = IntVar()
    comp_hiragana = IntVar()
    katakana = IntVar()
    mod_katakana = IntVar()
    comp_katakana = IntVar()
    rare_katakana = IntVar()

    type_label = Label(main_frame, text="Select the character types you would like to practice writing:", padx=50)

    katakana_check = Checkbutton(main_frame, text="katakana", variable=katakana)
    mod_katakana_check = Checkbutton(main_frame, text="modified katakana", variable=mod_katakana)
    comp_katakana_check = Checkbutton(main_frame, text="compound katakana", variable=comp_katakana)
    rare_katakana_check = Checkbutton(main_frame, text="rare katakana", variable=rare_katakana)
    hiragana_check = Checkbutton(main_frame, text="hiragana", variable=hiragana)
    mod_hiragana_check = Checkbutton(main_frame, text="modified hiragana", variable=mod_hiragana)
    comp_hiragana_check = Checkbutton(main_frame, text="compound hiragana", variable=comp_hiragana)

    type_label.grid(row=0, column=0)
    katakana_check.grid(row=1, column=0)
    hiragana_check.grid(row=2, column=0)
    mod_katakana_check.grid(row=3, column=0)
    comp_katakana_check.grid(row=4, column=0)
    rare_katakana_check.grid(row=5, column=0)
    mod_hiragana_check.grid(row=6, column=0)
    comp_hiragana_check.grid(row=7, column=0)

    session_button = Button(main_frame, text="Create Session", command=create_char_w_session, pady=10)

    session_button.grid(row=8, column=0, columnspan=1)


def create_char_w_session():
    # This function creates a session by creating a session list and calling the character session window function
    global main_frame
    global current

    session_list.clear()
    current = 0
    global katakana
    if katakana.get() == 1:
        for i in range(len(char_list)):
            if char_list[i].char_type == "katakana":
                session_list.append(char_list[i])
    if mod_katakana.get() == 1:
        for i in range(len(char_list)):
            if char_list[i].char_type == "mod katakana":
                session_list.append(char_list[i])
    if comp_katakana.get() == 1:
        for i in range(len(char_list)):
            if char_list[i].char_type == "comp katakana":
                session_list.append(char_list[i])
    if rare_katakana.get() == 1:
        for i in range(len(char_list)):
            if char_list[i].char_type == "rare katakana":
                session_list.append(char_list[i])
    global hiragana
    if hiragana.get() == 1:
        for i in range(len(char_list)):
            if char_list[i].char_type == "hiragana":
                session_list.append(char_list[i])
    if mod_hiragana.get() == 1:
        for i in range(len(char_list)):
            if char_list[i].char_type == "mod hiragana":
                session_list.append(char_list[i])
    if comp_hiragana.get() == 1:
        for i in range(len(char_list)):
            if char_list[i].char_type == "comp hiragana":
                session_list.append(char_list[i])

    shuffle_list(session_list)
    char_w_session_window()


def char_w_session_window():
    # This function runs the character writing trainer session
    global main_frame
    global new_button
    global prompt
    global feedback
    global show_button

    for widget in main_frame.winfo_children():
        widget.destroy()

    new_button = Button(main_frame, text="New Character", command=get_char_w)
    prompt = Label(main_frame, text="Select the new character button to start practicing", font=("Arial", 15))
    feedback = Label(main_frame, text="Press the show character button to reveal the character", font=("Arial", 15))
    show_button = Button(main_frame, text="Show Character", command=show_char_w)
    Button(main_frame, text="main menu", font=("Arial", 15), command=main_menu).grid(row=0, column=3)

    new_button.grid(row=0, column=0)
    prompt.grid(row=1, column=0, columnspan=2)
    feedback.grid(row=2, column=0, columnspan=2)
    show_button.grid(row=0, column=1)


def get_char_w():
    # this function gets a character from the session list and stores it in current char
    global current
    global main_frame
    global new_button
    global prompt
    global feedback
    global show_button
    global enter

    current = (current + 1) % len(session_list)
    prompt_text = "Draw the " + session_list[current].char_type + " character for " + session_list[current].romaji + ":"
    prompt.destroy()
    prompt = Label(main_frame, text=prompt_text, font=("Arial", 15))
    prompt.grid(row=1, column=0, columnspan=2)
    # The old prompt is erased and the prompt for the new character is created and displayed
    new_button["state"] = DISABLED
    show_button["state"] = NORMAL
    feedback.destroy()
    # The user is blocked from choosing a new word and the old feedback is removed to keep things running smooth


def show_char_w():
    # This function displays the current word
    global main_frame
    global current
    global feedback
    global show_button

    feedback.destroy()
    feedback = Label(main_frame, text=session_list[current].character, font=("IPAMincho", 80))
    feedback.grid(row=2, column=0, columnspan=2)
    show_button["state"] = DISABLED
    new_button["state"] = NORMAL


def get_word():
    # this function gets a word from the session list and stores it in current word
    global current
    global main_frame
    global new_button
    global prompt
    global feedback
    global show_button
    global enter
    global round_counter
    global round_total
    global curr_round
    global answer

    counter = len(session_list)
    current = (current + 1) % len(session_list)
    # This loop ensures that users will only receive characters that have not been correctly identified
    # 3 times in a row
    while session_list[current].num_correct > 2 and counter > 0:
        current = (current + 1) % len(session_list)
        counter -= 1
    # if all characters in the session list have been identified correctly 3 times in a row, they are all reset
    if counter == 0:
        for i in range(len(session_list)):
            session_list[i].num_correct = 0
            session_list[current].first_attempt = True
        end_message = "Session complete, you may keep studying or exit to start new session"
        end_label = Label(main_frame, text=end_message, font=("Arial", 15))
        end_label.grid(row=7, column=0, columnspan=3)
    round_counter = round_counter + 1
    if round_counter == round_total:
        round_counter = 0
        round_total = 0
        for i in session_list:
            if i.num_correct != 3:
                round_total += 1
    curr_round.destroy()
    round_string = "round progress:" + str(round_counter) + "/" + str(round_total)
    curr_round = Label(main_frame, text=round_string, font=("Arial", 15))
    curr_round.grid(row=5, column=1)
    prompt_text = "Enter the Japanese word for " + session_list[current].english + ":"
    # A random word is selected from the session list
    prompt.destroy()
    prompt = Label(main_frame, text=prompt_text, font=("Arial", 15))
    prompt.grid(row=2, column=0, columnspan=3)
    # The old prompt is erased and the prompt for the new word is created and displayed
    new_button["state"] = DISABLED
    show_button["state"] = NORMAL
    if session_type.get() == "test":
        enter["state"] = NORMAL
    feedback.destroy()
    # The user is blocked from choosing a new word and the old feedback is removed to keep things running smooth
    if session_type.get() == "flashcard":
        answer.destroy()


def test_entry():
    # This function checks whether the correct answer was entered
    global main_frame
    global input_box
    global new_button
    global feedback
    global answer
    global show_button
    global enter
    global progress

    current_entry = input_box.get()
    if current_entry == session_list[current].japanese:
        if session_list[current].first_attempt:
            session_list[current].num_correct = 3
        else:
            session_list[current].num_correct += 1
        counter = 0
        for i in range(len(session_list)):
            if session_list[i].num_correct == 3:
                counter += 1
        if progress.winfo_exists() == 1:
            progress.destroy()
        progress_string = "words learned: " + str(counter) + "/" + str(len(session_list))
        progress = Label(main_frame, text=progress_string, font=("Arial", 15))
        progress.grid(row=4, column=1)
        if feedback.winfo_exists() == 1:
            feedback.destroy()
        if answer.winfo_exists() == 1:
            answer.destroy()
        feedback = Label(main_frame, text="correct", font=("Arial", 15))
        feedback.grid(row=3, column=0, columnspan=3)
        input_box.delete(0, "end")
        new_button["state"] = NORMAL
        enter["state"] = DISABLED
    else:
        session_list[current].num_correct = 0
        if session_list[current].first_attempt:
            session_list[current].first_attempt = False
        if feedback.winfo_exists() == 1:
            feedback.destroy()
        feedback = Label(main_frame, text="incorrect", font=("Arial", 15))
        feedback.grid(row=3, column=0, columnspan=3)


session_list = []


def show_answer():
    # This function displays the current word
    global main_frame
    global current
    global answer
    global show_button
    global new_button

    session_list[current].num_correct = 0
    if session_list[current].first_attempt:
        session_list[current].first_attempt = False
    answer = Label(main_frame, text=session_list[current].japanese, font=("Arial", 15))
    answer.grid(row=6, column=0, columnspan=3)
    show_button["state"] = DISABLED
    if session_type.get() == "flashcard":
        new_button["state"] = NORMAL


def create_vocab_session(list_units):
    # This function creates a session by creating a session list and calling the vocab session window function
    global main_frame
    global current

    session_list.clear()
    current = 0
    for unit in list_units:
        global noun
        if noun.get() == 1:
            for i in range(len(vocab_list)):
                if vocab_list[i].type == "noun" and vocab_list[i].unit == unit.get():
                    session_list.append(vocab_list[i])
        global pronoun
        if pronoun.get() == 1:
            for i in range(len(vocab_list)):
                if vocab_list[i].type == "pronoun" and vocab_list[i].unit == unit.get():
                    session_list.append(vocab_list[i])
        global title
        if title.get() == 1:
            for i in range(len(vocab_list)):
                if vocab_list[i].type == "title" and vocab_list[i].unit == unit.get():
                    session_list.append(vocab_list[i])
        global adjective
        if adjective.get() == 1:
            for i in range(len(vocab_list)):
                if vocab_list[i].type == "adjective" and vocab_list[i].unit == unit.get():
                    session_list.append(vocab_list[i])
        global adverb
        if adverb.get() == 1:
            for i in range(len(vocab_list)):
                if vocab_list[i].type == "adverb" and vocab_list[i].unit == unit.get():
                    session_list.append(vocab_list[i])
        global preposition
        if preposition.get() == 1:
            for i in range(len(vocab_list)):
                if vocab_list[i].type == "preposition" and vocab_list[i].unit == unit.get():
                    session_list.append(vocab_list[i])
        global time
        if time.get() == 1:
            for i in range(len(vocab_list)):
                if vocab_list[i].type == "time" and vocab_list[i].unit == unit.get():
                    session_list.append(vocab_list[i])
        global question
        if question.get() == 1:
            for i in range(len(vocab_list)):
                if vocab_list[i].type == "question" and vocab_list[i].unit == unit.get():
                    session_list.append(vocab_list[i])
        global verb
        if verb.get() == 1:
            for i in range(len(vocab_list)):
                if vocab_list[i].type == "verb" and vocab_list[i].unit == unit.get():
                    session_list.append(vocab_list[i])
        global expression
        if expression.get() == 1:
            for i in range(len(vocab_list)):
                if vocab_list[i].type == "expressions" and vocab_list[i].unit == unit.get():
                    session_list.append(vocab_list[i])

    shuffle_list(session_list)
    vocab_session_window()


def vocab_session_window():
    # This function runs the vocab trainer session
    global main_frame
    global new_button
    global prompt
    global feedback
    global answer
    global input_box
    global show_button
    global enter
    global progress
    global round_total
    global round_counter
    global curr_round
    global session_type

    for widget in main_frame.winfo_children():
        widget.destroy()

    round_total = len(session_list)
    round_counter = -1

    input_box = Entry(main_frame, font=("Arial", 30))
    enter = Button(main_frame, text="Enter", command=test_entry)
    if session_type.get() == "flashcard":
        enter["state"] = DISABLED
    feedback = Label(main_frame, text="Press the enter button to test your answer", font=("Arial", 15))
    progress_string = "words learned: 0/" + str(len(session_list))
    progress = Label(main_frame, text=progress_string, font=("Arial", 15))

    new_button = Button(main_frame, text="New Word", command=get_word)
    prompt = Label(main_frame, text="Select the new word button to start practicing", font=("Arial", 15))
    show_button = Button(main_frame, text="Show Answer", command=show_answer)
    answer = Label(main_frame, text="", font=("Arial", 15))
    round_string = "round progress:" + str(round_counter) + "/" + str(round_total)
    curr_round = Label(main_frame, text=round_string, font=("Arial", 15))
    Button(main_frame, text="main menu", font=("Arial", 15), command=main_menu).grid(row=0, column=3)

    input_box.grid(row=0, column=0, columnspan=3)
    enter.grid(row=1, column=2)
    feedback.grid(row=3, column=0, columnspan=3)
    progress.grid(row=4, column=1)

    new_button.grid(row=1, column=0)
    prompt.grid(row=2, column=0, columnspan=3)
    show_button.grid(row=1, column=1)
    curr_round.grid(row=5, column=1)


def vocab_menu():
    # This function creates the menu that allows user to customize their vocab session
    global noun
    global pronoun
    global title
    global adjective
    global adverb
    global preposition
    global time
    global question
    global verb
    global expression
    global root
    global session_type

    for widget in main_frame.winfo_children():
        widget.destroy()

    noun = IntVar()
    pronoun = IntVar()
    title = IntVar()
    adjective = IntVar()
    adverb = IntVar()
    preposition = IntVar()
    time = IntVar()
    question = IntVar()
    verb = IntVar()
    expression = IntVar()
    unit_1 = StringVar()
    unit_2 = StringVar()
    unit_3 = StringVar()
    unit_4 = StringVar()
    unit_5 = StringVar()
    unit_6 = StringVar()
    unit_7 = StringVar()
    unit_8 = StringVar()
    unit_9 = StringVar()
    unit_10 = StringVar()
    unit_11 = StringVar()
    unit_12 = StringVar()
    bonus_1 = StringVar()
    session_type = StringVar()
    session_type.set("flashcard")

    unit_list = [unit_1,
                 unit_2,
                 unit_3,
                 unit_4,
                 unit_5,
                 unit_6,
                 unit_7,
                 unit_8,
                 unit_9,
                 unit_10,
                 unit_11,
                 unit_12,
                 bonus_1]

    type_label = Label(main_frame, text="Select the word types you would like to study:", padx=50)
    unit_label = Label(main_frame, text="Select the units you would like to study:", padx=50)
    session_label = Label(main_frame, text="Select which session type you would like:", padx=50)

    noun_check = Checkbutton(main_frame, text="noun", variable=noun)
    pronoun_check = Checkbutton(main_frame, text="pronoun", variable=pronoun)
    title_check = Checkbutton(main_frame, text="title", variable=title)
    adjective_check = Checkbutton(main_frame, text="adjective", variable=adjective)
    adverb_check = Checkbutton(main_frame, text="adverb", variable=adverb)
    preposition_check = Checkbutton(main_frame, text="preposition", variable=preposition)
    time_check = Checkbutton(main_frame, text="time", variable=time)
    question_check = Checkbutton(main_frame, text="question", variable=question)
    verb_check = Checkbutton(main_frame, text="verb", variable=verb)
    expression_check = Checkbutton(main_frame, text="expression", variable=expression)

    flashcard = Radiobutton(main_frame, text="flashcards", variable=session_type, value="flashcard")
    test_session = Radiobutton(main_frame, text="test", variable=session_type, value="test")

    session_label.grid(row=0, column=2)
    flashcard.grid(row=1, column=2)
    test_session.grid(row=2, column=2)

    type_label.grid(row=0, column=1)
    noun_check.grid(row=1, column=1)
    pronoun_check.grid(row=2, column=1)
    title_check.grid(row=3, column=1)
    adjective_check.grid(row=4, column=1)
    adverb_check.grid(row=5, column=1)
    preposition_check.grid(row=6, column=1)
    time_check.grid(row=7, column=1)
    question_check.grid(row=8, column=1)
    verb_check.grid(row=9, column=1)
    expression_check.grid(row=10, column=1)

    unit_1_check = Checkbutton(main_frame, text="unit 1", variable=unit_1, onvalue="unit 1", offvalue="")
    unit_2_check = Checkbutton(main_frame, text="unit 2", variable=unit_2, onvalue="unit 2", offvalue="")
    unit_3_check = Checkbutton(main_frame, text="unit 3", variable=unit_3, onvalue="unit 3", offvalue="")
    unit_4_check = Checkbutton(main_frame, text="unit 4", variable=unit_4, onvalue="unit 4", offvalue="")
    unit_5_check = Checkbutton(main_frame, text="unit 5", variable=unit_5, onvalue="unit 5", offvalue="")
    unit_6_check = Checkbutton(main_frame, text="unit 6", variable=unit_6, onvalue="unit 6", offvalue="")
    unit_7_check = Checkbutton(main_frame, text="unit 7", variable=unit_7, onvalue="unit 7", offvalue="")
    unit_8_check = Checkbutton(main_frame, text="unit 8", variable=unit_8, onvalue="unit 8", offvalue="")
    unit_9_check = Checkbutton(main_frame, text="unit 9", variable=unit_9, onvalue="unit 9", offvalue="")
    unit_10_check = Checkbutton(main_frame, text="unit 10", variable=unit_10, onvalue="unit 10", offvalue="")
    unit_11_check = Checkbutton(main_frame, text="unit 11", variable=unit_11, onvalue="unit 11", offvalue="")
    unit_12_check = Checkbutton(main_frame, text="unit 12", variable=unit_12, onvalue="unit 12", offvalue="")
    bonus_1_check = Checkbutton(main_frame, text="bonus 1", variable=bonus_1, onvalue="bonus 1", offvalue="")

    unit_label.grid(row=0, column=0)
    unit_1_check.grid(row=1, column=0)
    unit_2_check.grid(row=2, column=0)
    unit_3_check.grid(row=3, column=0)
    unit_4_check.grid(row=4, column=0)
    unit_5_check.grid(row=5, column=0)
    unit_6_check.grid(row=6, column=0)
    unit_7_check.grid(row=7, column=0)
    unit_8_check.grid(row=8, column=0)
    unit_9_check.grid(row=9, column=0)
    unit_10_check.grid(row=10, column=0)
    unit_11_check.grid(row=11, column=0)
    unit_12_check.grid(row=12, column=0)
    bonus_1_check.grid(row=13, column=0)

    unit_1_check.deselect()
    unit_2_check.deselect()
    unit_3_check.deselect()
    unit_4_check.deselect()
    unit_5_check.deselect()
    unit_6_check.deselect()
    unit_7_check.deselect()
    unit_8_check.deselect()
    unit_9_check.deselect()
    unit_10_check.deselect()
    unit_11_check.deselect()
    unit_12_check.deselect()
    bonus_1_check.deselect()

    session_button = Button(main_frame, text="Create Session", command=lambda: create_vocab_session(unit_list), pady=10)

    session_button.grid(row=14, column=0, columnspan=4)


def particle_menu():
    # This function runs a window where the user can customize their particle practice session

    global main_frame

    for widget in main_frame.winfo_children():
        widget.destroy()

    part_label = Label(main_frame, text="Select the particles you would like to study:", padx=50)
    part_label.grid(row=0, column=0, columnspan=2)

    wa = StringVar()
    no = StringVar()
    ka = StringVar()
    mo = StringVar()
    ne = StringVar()
    yo = StringVar()
    ni = StringVar()
    o = StringVar()
    de = StringVar()
    ga = StringVar()
    he = StringVar()
    to = StringVar()

    particle_list = [wa,
                     no,
                     ka,
                     mo,
                     ne,
                     yo,
                     ni,
                     o,
                     de,
                     ga,
                     he,
                     to]

    wa_check = Checkbutton(main_frame, text="wa (は)", variable=wa, onvalue="は", offvalue="")
    no_check = Checkbutton(main_frame, text="no (の)", variable=no, onvalue="の", offvalue="")
    ka_check = Checkbutton(main_frame, text="ka (か)", variable=ka, onvalue="か", offvalue="")
    mo_check = Checkbutton(main_frame, text="mo (も)", variable=mo, onvalue="も", offvalue="")
    ne_check = Checkbutton(main_frame, text="ne (ね)", variable=ne, onvalue="ね", offvalue="")
    yo_check = Checkbutton(main_frame, text="yo (よ)", variable=yo, onvalue="よ", offvalue="")
    ni_check = Checkbutton(main_frame, text="ni (に)", variable=ni, onvalue="に", offvalue="")
    o_check = Checkbutton(main_frame, text="o (を)", variable=o, onvalue="を", offvalue="")
    de_check = Checkbutton(main_frame, text="de (で)", variable=de, onvalue="で", offvalue="")
    ga_check = Checkbutton(main_frame, text="ga (が)", variable=ga, onvalue="が", offvalue="")
    he_check = Checkbutton(main_frame, text="he (へ)", variable=he, onvalue="へ", offvalue="")
    to_check = Checkbutton(main_frame, text="to (と)", variable=to, onvalue="と", offvalue="")

    wa_check.grid(row=1, column=0)
    no_check.grid(row=2, column=0)
    ka_check.grid(row=3, column=0)
    mo_check.grid(row=4, column=0)
    ne_check.grid(row=5, column=0)
    yo_check.grid(row=6, column=0)
    ni_check.grid(row=1, column=1)
    o_check.grid(row=2, column=1)
    de_check.grid(row=3, column=1)
    ga_check.grid(row=4, column=1)
    he_check.grid(row=5, column=1)
    to_check.grid(row=6, column=1)

    wa_check.deselect()
    no_check.deselect()
    ka_check.deselect()
    mo_check.deselect()
    ne_check.deselect()
    yo_check.deselect()
    ni_check.deselect()
    o_check.deselect()
    de_check.deselect()
    ga_check.deselect()
    he_check.deselect()
    to_check.deselect()

    session_button_def = Button(main_frame, text="Practice Definitions",
                                command=lambda: create_part_def_ses(particle_list), pady=10)
    session_button_use = Button(main_frame, text="Practice Usage",
                                command=lambda: create_part_use_ses(particle_list), pady=10)

    session_button_def.grid(row=7, column=0)
    session_button_use.grid(row=7, column=1)


def create_part_def_ses(p_list):
    # This function creates a session by creating a session list and calling the particle definition
    # session window function
    global main_frame
    global current

    session_list.clear()
    current = 0
    for p in p_list:
        if p.get() != "":
            for i in part_list:
                if i.character == p.get():
                    session_list.append(i)

    shuffle_list(session_list)
    part_def_ses_win()


def part_def_ses_win():
    # This function runs the particle definition trainer session
    global main_frame
    global new_button
    global prompt
    global feedback
    global answer
    global show_button
    global enter
    global input_box

    for widget in main_frame.winfo_children():
        widget.destroy()

    new_button = Button(main_frame, text="New Particle", command=get_part_def)
    input_box = Entry(main_frame, font=("Arial", 30))
    enter = Button(main_frame, text="Enter", command=test_part_def)
    prompt = Label(main_frame, text="Select the new particle to start practicing", font=("Arial", 15))
    feedback = Label(main_frame, text="Press the enter button to test your answer", font=("Arial", 15))
    show_button = Button(main_frame, text="Show Answer", command=show_part_def)
    answer = Label(main_frame, text="", font=("Arial", 15))
    Button(main_frame, text="main menu", font=("Arial", 15), command=main_menu).grid(row=0, column=3)

    new_button.grid(row=1, column=0)
    input_box.grid(row=0, column=0, columnspan=3)
    enter.grid(row=1, column=2)
    prompt.grid(row=2, column=0, columnspan=3)
    feedback.grid(row=3, column=0, columnspan=3)
    show_button.grid(row=1, column=1)


def get_part_def():
    # this function gets a particle from the session list and stores its index in current
    global current
    global main_frame
    global new_button
    global prompt
    global feedback
    global show_button
    global enter

    current = random.randint(0, len(session_list) - 1)
    use = random.randint(0, len(session_list[current].uses) - 1)
    prompt_text = "Enter the particle that " + session_list[current].uses[use] + ":"
    # A random particle is selected from the session list
    prompt.destroy()
    prompt = Label(main_frame, text=prompt_text, font=("Arial", 15))
    prompt.grid(row=2, column=0, columnspan=3)
    # The old prompt is erased and the prompt for the new word is created and displayed
    new_button["state"] = DISABLED
    show_button["state"] = NORMAL
    enter["state"] = NORMAL
    feedback.destroy()
    # The user is blocked from choosing a new word and the old feedback is removed to keep things running smooth


def test_part_def():
    # This function checks whether the correct answer was entered
    global main_frame
    global input_box
    global new_button
    global feedback
    global answer
    global show_button
    global enter

    current_entry = input_box.get()
    if current_entry == session_list[current].character:
        if feedback.winfo_exists() == 1:
            feedback.destroy()
        if answer.winfo_exists() == 1:
            answer.destroy()
        feedback = Label(main_frame, text="correct", font=("Arial", 15))
        feedback.grid(row=3, column=0, columnspan=3)
        input_box.delete(0, "end")
        new_button["state"] = NORMAL
        enter["state"] = DISABLED
    else:
        if feedback.winfo_exists() == 1:
            feedback.destroy()
        feedback = Label(main_frame, text="incorrect", font=("Arial", 15))
        feedback.grid(row=3, column=0, columnspan=3)


def show_part_def():
    # This function displays the current particle
    global main_frame
    global current
    global answer
    global show_button

    answer = Label(main_frame, text=session_list[current].character, font=("Arial", 15))
    answer.grid(row=4, column=0, columnspan=3)
    show_button["state"] = DISABLED


def create_part_use_ses(p_list):
    # This function creates a session by creating a session list and calling the particle usage
    # session window function
    global main_frame
    global current

    session_list.clear()
    current = 0
    for p in p_list:
        if p.get() != "":
            for i in part_list:
                if i.character == p.get():
                    session_list.append(i)

    shuffle_list(session_list)
    session_list.append(Particle("X", ["No particle"]))
    part_use_ses_win()


def part_use_ses_win():
    # This function runs the particle definition trainer session
    global main_frame
    global new_button
    global prompt
    global feedback
    global answer
    global show_button
    global enter
    global input_box

    for widget in main_frame.winfo_children():
        widget.destroy()

    new_button = Button(main_frame, text="New Particle", command=get_part_use)
    input_box = Entry(main_frame, font=("Arial", 30))
    enter = Button(main_frame, text="Enter", command=test_part_def)
    prompt = Label(main_frame, text="Select the new particle to start practicing", font=("Arial", 15))
    feedback = Label(main_frame, text="Press the enter button to test your answer", font=("Arial", 15))
    show_button = Button(main_frame, text="Show Answer", command=show_part_def)
    answer = Label(main_frame, text="", font=("Arial", 15))
    Button(main_frame, text="main menu", font=("Arial", 15), command=main_menu).grid(row=0, column=3)


    new_button.grid(row=1, column=0)
    input_box.grid(row=0, column=0, columnspan=3)
    enter.grid(row=1, column=2)
    prompt.grid(row=2, column=0, columnspan=3)
    feedback.grid(row=3, column=0, columnspan=3)
    show_button.grid(row=1, column=1)


def get_part_use():
    # this function gets a particle from the session list and stores its index in current
    global current
    global main_frame
    global new_button
    global prompt
    global feedback
    global show_button
    global enter

    current = random.randint(0, len(session_list) - 1)
    prompt_text = "Enter the particle that belongs at ? (X for none)\n" + gen_sentence_particle()
    # A random particle is selected from the session list
    prompt.destroy()
    prompt = Label(main_frame, text=prompt_text, font=("Arial", 15))
    prompt.grid(row=2, column=0, columnspan=3)
    # The old prompt is erased and the prompt for the new word is created and displayed
    new_button["state"] = DISABLED
    show_button["state"] = NORMAL
    enter["state"] = NORMAL
    feedback.destroy()
    # The user is blocked from choosing a new word and the old feedback is removed to keep things running smooth


def gen_sentence_particle():
    global current

    names = ["メアリさん",
             "ソラさん",
             "けんさん",
             "たけしさん",
             "わたし"]

    people_desu = ["にほんじん",
                   "アメリカじん",
                   "いちねんせい",
                   "にねんせい",
                   "さんねんせい",
                   "よんねんせい",
                   "がくせい",
                   "せんせい",
                   "べんごし",
                   "かんごし",
                   "いしゃ"]

    majors = ["えいご",
              "アジアけんきゅう",
              "けいざい",
              "こうがく",
              "コンピューター",
              "せいじ",
              "せいぶつがく",
              "ビジネス",
              "ぶんがく",
              "れきし",
              "こくさいかんけい"]

    foods = ["さかな",
             "くだもの",
             "とんかつ",
             "アイスクリーム",
             "ハンバーガー",
             "やさい"]

    places = ["だいがく",
              "がっこう",
              "コンビニ",
              "としょかん",
              "アメリカ",
              "にほん"]

    days = ["どようび",
            "にちようび",
            "げつようび",
            "かようび",
            "もくようび",
            "きんようび",
            "すいようび"]

    if session_list[current].character == "X":
        name = names[random.randint(0, len(names) - 1)]
        desu = people_desu[random.randint(0, len(people_desu) - 1)]
        return name + "は" + desu + "?です"

    if session_list[current].character == "は":
        name = names[random.randint(0, len(names) - 1)]
        desu = people_desu[random.randint(0, len(people_desu) - 1)]
        return name + "?" + desu + "です"

    if session_list[current].character == "の":
        name = names[random.randint(0, len(names) - 1)]
        major = majors[random.randint(0, len(majors) - 1)]
        return name + "?" + "せんこうは" + major + "です"

    if session_list[current].character == "か":
        return "せんこうはなんです?"

    if session_list[current].character == "も":
        name = names[random.randint(0, len(names) - 1)]
        name_2 = names[random.randint(0, len(names) - 1)]
        while name == name_2:
            name_2 = names[random.randint(0, len(names) - 1)]
        desu = people_desu[random.randint(0, len(people_desu) - 1)]
        return name + "は" + desu + "です。" + name_2 + "?" + desu + "です"

    # if session_list[current].character == "ね":
    #  return ""

    # if session_list[current].character == "よ":
    # return ""

    if session_list[current].character == "に":
        cur_day = days[random.randint(0, len(days) - 1)]
        place = places[random.randint(0, len(places) - 1)]
        return cur_day + "?" + place + "へ" + "いきます"

    if session_list[current].character == "を":
        food = foods[random.randint(0, len(foods) - 1)]
        return food + "?たべます"

    if session_list[current].character == "で":
        name = names[random.randint(0, len(names) - 1)]
        place = places[random.randint(0, len(places) - 1)]
        return name + "は" + place + "?にほんごをべんきょうします"

    if session_list[current].character == "が":
        name = names[random.randint(0, len(names) - 1)]
        food = foods[random.randint(0, len(foods) - 1)]
        return name + "は" + food + "?すきです"

    if session_list[current].character == "へ":
        name = names[random.randint(0, len(names) - 1)]
        place = places[random.randint(0, len(places) - 1)]
        return name + "は" + place + "?いきます"

    if session_list[current].character == "と":
        name = names[random.randint(0, len(names) - 1)]
        place = places[random.randint(0, len(places) - 1)]
        place_2 = places[random.randint(0, len(places) - 1)]
        while name == place_2:
            place_2 = places[random.randint(0, len(places) - 1)]
        return name + "は" + place + "?" + place_2 + "へいきます"


def num_menu():
    # This function creates the menu that allows user to customize their number session
    global main_frame
    global session_type
    global session_type_alt

    for widget in main_frame.winfo_children():
        widget.destroy()

    session_type_alt = StringVar()
    session_type_alt.set("hiragana")
    session_type = StringVar()
    session_type.set("flashcard")

    session_alt_label = Label(main_frame, text="Select the number character type you would like to study:", padx=50)
    session_label = Label(main_frame, text="Select which session type you would like:", padx=50)

    flashcard = Radiobutton(main_frame, text="flashcards", variable=session_type, value="flashcard")
    test_session = Radiobutton(main_frame, text="test", variable=session_type, value="test")

    hiragana_button = Radiobutton(main_frame, text="hiragana", variable=session_type_alt, value="hiragana")
    kanji_button = Radiobutton(main_frame, text="kanji", variable=session_type_alt, value="kanji")

    session_alt_label.grid(row=0, column=0)
    hiragana_button.grid(row=1, column=0)
    kanji_button.grid(row=2, column=0)

    session_label.grid(row=0, column=1)
    flashcard.grid(row=1, column=1)
    test_session.grid(row=2, column=1)

    session_button = Button(main_frame, text="Create Session", command=numbers, pady=10)

    session_button.grid(row=3, column=0, columnspan=2)


def numbers():
    # this function runs the number practice window
    global prompt
    global feedback
    global main_frame
    global new_button
    global answer
    global show_button

    for widget in main_frame.winfo_children():
        widget.destroy()

    new_button = Button(main_frame, text="New number", command=get_number)
    global input_box
    input_box = Entry(main_frame, font=("Arial", 30), width=35)
    enter_num = Button(main_frame, text="Enter", command=test_num)
    if session_type.get() == "flashcard":
        enter_num["state"] = DISABLED
    prompt = Label(main_frame, text="Select the new number button to start practicing", font=("Arial", 15))
    feedback = Label(main_frame, text="Press the enter button to test your answer", font=("Arial", 15))
    show_button = Button(main_frame, text="Show Answer", command=show_num)
    answer = Label(main_frame, text="", font=("Arial", 15))
    Button(main_frame, text="main menu", font=("Arial", 15), command=main_menu).grid(row=0, column=3)

    new_button.grid(row=1, column=0)
    input_box.grid(row=0, column=0, columnspan=3)
    enter_num.grid(row=1, column=2)
    prompt.grid(row=2, column=0, columnspan=3)
    feedback.grid(row=3, column=0, columnspan=3)
    show_button.grid(row=1, column=1)


def get_number():
    # this function creates the number for the number trainer
    global current_num
    global main_frame
    global new_button
    global prompt
    global feedback

    current_num = random.randint(0, 99999)
    prompt_text = ""
    if session_type_alt.get() == "hiragana":
        prompt_text = "Enter the Hiragana for " + str(current_num) + ":"
    if session_type_alt.get() == "kanji":
        prompt_text = "Enter the Hiragana for " + num_kanji(str(current_num)) + ":"
    prompt.destroy()
    prompt = Label(main_frame, text=prompt_text, font=("Arial", 15))
    prompt.grid(row=2, column=0, columnspan=3)
    new_button["state"] = DISABLED
    show_button["state"] = NORMAL
    feedback.destroy()
    if session_type.get() == "flashcard":
        answer.destroy()


def test_num():
    # this function checks to see if the entry is correct
    global main_frame
    global input_box
    global new_button
    global feedback
    global current_num

    current_entry = input_box.get()
    if current_entry == num_convert(str(current_num)):
        if feedback.winfo_exists() == 1:
            feedback.destroy()
        feedback = Label(main_frame, text="correct", font=("Arial", 15))
        feedback.grid(row=3, column=0, columnspan=3)
        input_box.delete(0, "end")
        new_button["state"] = NORMAL
    else:
        if feedback.winfo_exists() == 1:
            feedback.destroy()
        feedback = Label(main_frame, text="incorrect", font=("Arial", 15))
        feedback.grid(row=3, column=0, columnspan=3)


def show_num():
    # This function displays the current number
    global main_frame
    global current_num
    global answer
    global show_button

    if answer.winfo_exists() == 1:
        answer.destroy()
    answer = Label(main_frame, text=num_convert(str(current_num)), font=("Arial", 15))
    answer.grid(row=4, column=0, columnspan=3)
    show_button["state"] = DISABLED
    if session_type.get() == "flashcard":
        new_button["state"] = NORMAL


def num_convert(number):
    # This function converts an arabic number into a hiragana number
    converted = ""
    counter = len(number)
    num_dict = {"2": "に",
                "3": "さん",
                "4": "よん",
                "5": "ご",
                "6": "ろく",
                "7": "なな",
                "8": "はち",
                "9": "きゅう"}

    place_dict = {1: "",
                  2: "じゅう",
                  3: "ひゃく",
                  4: "せん",
                  5: "まん"}

    if number == "0":
        converted += "ゼロ"

    for i in range(len(number)):
        if counter == 3 and number[i] == "3":
            converted += "さんびゃく"
        elif counter == 3 and number[i] == "6":
            converted += "ろっぴゃく"
        elif counter == 3 and number[i] == "8":
            converted += "はっぴゃく"
        elif counter == 4 and number[i] == "3":
            converted += "さんぜん"
        elif counter == 4 and number[i] == "8":
            converted += "はっせん"
        elif counter == 5 and number[i] == "1":
            converted += "いちまん"
        else:
            if number[i] != "1" and number[i] != "0":
                converted += num_dict[number[i]]
            if number[i] != "0":
                converted += place_dict[counter]
        counter -= 1

    if number[len(number) - 1] == "1":
        converted += "いち"

    return converted


def num_kanji(number):
    # This function converts an arabic number into a hiragana number
    converted = ""
    counter = len(number)
    num_dict = {"2": "二",
                "3": "三",
                "4": "四",
                "5": "五",
                "6": "六",
                "7": "七",
                "8": "八",
                "9": "九"}

    place_dict = {1: "",
                  2: "十",
                  3: "百",
                  4: "千",
                  5: "万"}

    if number == "0":
        converted += "ゼロ"

    for i in range(len(number)):
        if counter == 5 and number[i] == "1":
            converted += "一万"
        else:
            if number[i] != "1" and number[i] != "0":
                converted += num_dict[number[i]]
            if number[i] != "0":
                converted += place_dict[counter]
        counter -= 1

    if number[len(number) - 1] == "1":
        converted += "ー"

    return converted


def time_menu():
    # This function creates the menu that allows user to customize their number session
    global main_frame
    global session_type
    global session_type_alt

    for widget in main_frame.winfo_children():
        widget.destroy()

    session_type_alt = StringVar()
    session_type_alt.set("hiragana")
    session_type = StringVar()
    session_type.set("flashcard")

    session_alt_label = Label(main_frame, text="Select the time character type you would like to study:", padx=50)
    session_label = Label(main_frame, text="Select which session type you would like:", padx=50)

    flashcard = Radiobutton(main_frame, text="flashcards", variable=session_type, value="flashcard")
    test_session = Radiobutton(main_frame, text="test", variable=session_type, value="test")

    hiragana_button = Radiobutton(main_frame, text="hiragana", variable=session_type_alt, value="hiragana")
    kanji_button = Radiobutton(main_frame, text="kanji", variable=session_type_alt, value="kanji")

    session_alt_label.grid(row=0, column=0)
    hiragana_button.grid(row=1, column=0)
    kanji_button.grid(row=2, column=0)

    session_label.grid(row=0, column=1)
    flashcard.grid(row=1, column=1)
    test_session.grid(row=2, column=1)

    session_button = Button(main_frame, text="Create Session", command=time_session_window, pady=10)

    session_button.grid(row=3, column=0, columnspan=2)


def time_session_window():
    # This function runs the time window
    global main_frame
    global new_button
    global input_box
    global prompt
    global feedback
    global answer
    global show_button
    global enter

    for widget in main_frame.winfo_children():
        widget.destroy()

    new_button = Button(main_frame, text="New time", command=get_time)
    input_box = Entry(main_frame, font=("Arial", 30), width=35)
    enter = Button(main_frame, text="Enter", command=test_time)
    if session_type.get() == "flashcard":
        enter["state"] = DISABLED
    prompt = Label(main_frame, text="Select the new time button to start practicing", font=("Arial", 15))
    feedback = Label(main_frame, text="Press the enter button to test your answer", font=("Arial", 15))
    show_button = Button(main_frame, text="Show Answer", command=show_time)
    answer = Label(main_frame, text="", font=("Arial", 15))
    Button(main_frame, text="main menu", font=("Arial", 15), command=main_menu).grid(row=0, column=3)

    new_button.grid(row=1, column=0)
    input_box.grid(row=0, column=0, columnspan=3)
    enter.grid(row=1, column=2)
    prompt.grid(row=2, column=0, columnspan=3)
    feedback.grid(row=3, column=0, columnspan=3)
    show_button.grid(row=1, column=1)


def get_time():
    # This function provides a random time for the time trainer
    global current_time
    global main_frame
    global new_button
    global prompt
    global feedback

    hours = str(random.randint(1, 12))
    minutes = str(random.randint(0, 59))
    if len(minutes) == 1:
        minutes = "0" + minutes
    current_time = hours + ":" + minutes
    prompt_text = ""
    if session_type_alt.get() == "hiragana":
        prompt_text = "Enter the Hiragana for " + current_time
    if session_type_alt.get() == "kanji":
        prompt_text = "Enter the Hiragana for " + time_kanji(current_time)
    prompt.destroy()
    prompt = Label(main_frame, text=prompt_text, font=("Arial", 15))
    prompt.grid(row=2, column=0, columnspan=3)
    new_button["state"] = DISABLED
    show_button["state"] = NORMAL
    feedback.destroy()
    if session_type.get() == "flashcard":
        answer.destroy()


def test_time():
    # This function tests whether the entry is correct for the time trainer
    global main_frame
    global input_box
    global new_button
    global feedback
    global current_time

    current_entry = input_box.get()
    if current_entry == time_convert(current_time):
        if feedback.winfo_exists() == 1:
            feedback.destroy()
        feedback = Label(main_frame, text="correct", font=("Arial", 15))
        feedback.grid(row=3, column=0, columnspan=3)
        input_box.delete(0, "end")
        new_button["state"] = NORMAL
    else:
        if feedback.winfo_exists() == 1:
            feedback.destroy()
        feedback = Label(main_frame, text="incorrect", font=("Arial", 15))
        feedback.grid(row=3, column=0, columnspan=3)


def show_time():
    # This function displays the current time
    global main_frame
    global current_time
    global answer
    global show_button

    answer = Label(main_frame, text=time_convert(current_time), font=("Arial", 15))
    answer.grid(row=4, column=0, columnspan=3)
    show_button["state"] = DISABLED
    if session_type.get() == "flashcard":
        new_button["state"] = NORMAL


def time_convert(cur_tim):
    # This function turns an english date into a japanese date
    converted = ""
    hours = ""
    minutes = ""
    minute = False

    for i in cur_tim:
        if i == ":":
            minute = True
        elif not minute:
            hours += i
        elif minute:
            minutes += i

    hours_dict = {"1": "いちじ",
                  "2": "にじ",
                  "3": "さんじ",
                  "4": "よじ",
                  "5": "ごじ",
                  "6": "ろくじ",
                  "7": "しちじ",
                  "8": "はちじ",
                  "9": "くじ",
                  "10": "じゅうじ",
                  "11": "じゅういちじ",
                  "12": "じゅうにじ"}

    min_dict = {"1": "いっぷん",
                "2": "にふん",
                "3": "さんぷん",
                "4": "よんぷん",
                "5": "ごふん",
                "6": "ろっぷん",
                "7": "ななふん",
                "8": "はっぷん",
                "9": "きゅうふん",
                "10": "じゅっぷん"}

    min_dict_2 = {"2": "に",
                  "3": "さん",
                  "4": "よん",
                  "5": "ご",
                  "6": "ろく"}

    min_dict_3 = {"1": "じゅう",
                  "2": "にじゅう",
                  "3": "さんじゅう",
                  "4": "よんじゅう",
                  "5": "ごじゅう"}

    converted += hours_dict[hours]

    if minutes[0] == "0" and minutes[1] != "0":
        converted += min_dict[minutes[1]]

    elif minutes[0] != "0" and minutes[1] == "0":
        if minutes[0] != "1":
            converted += min_dict_2[minutes[0]]
        converted += min_dict["10"]

    elif minutes[0] != "0" and minutes[1] != "0":
        converted += min_dict_3[minutes[0]]
        converted += min_dict[minutes[1]]

    return converted


def time_kanji(cur_tim):
    # This function turns an english date into a japanese date
    converted = ""
    hours = ""
    minutes = ""
    minute = False

    for i in cur_tim:
        if i == ":":
            minute = True
        elif not minute:
            hours += i
        elif minute:
            minutes += i

    hours_dict = {"1": "一時",
                  "2": "二時",
                  "3": "三時",
                  "4": "四時",
                  "5": "五時",
                  "6": "六時",
                  "7": "七時",
                  "8": "八時",
                  "9": "九時",
                  "10": "十時",
                  "11": "十一時",
                  "12": "十二時"}

    min_dict = {"1": "一分",
                "2": "二分",
                "3": "三分",
                "4": "四分",
                "5": "五分",
                "6": "六分",
                "7": "七分",
                "8": "八分",
                "9": "九分",
                "10": "十分"}

    min_dict_2 = {"2": "二",
                  "3": "三",
                  "4": "四",
                  "5": "五",
                  "6": "六"}

    min_dict_3 = {"1": "十",
                  "2": "二十",
                  "3": "三十",
                  "4": "四十",
                  "5": "五十"}

    converted += hours_dict[hours]

    if minutes[0] == "0" and minutes[1] != "0":
        converted += min_dict[minutes[1]]

    elif minutes[0] != "0" and minutes[1] == "0":
        if minutes[0] != "1":
            converted += min_dict_2[minutes[0]]
        converted += min_dict["10"]

    elif minutes[0] != "0" and minutes[1] != "0":
        converted += min_dict_3[minutes[0]]
        converted += min_dict[minutes[1]]

    return converted


def calendar_menu():
    # This function creates the menu that allows user to customize their calendar session
    global main_frame
    global session_type
    global session_type_alt

    for widget in main_frame.winfo_children():
        widget.destroy()

    session_type_alt = StringVar()
    session_type_alt.set("hiragana")
    session_type = StringVar()
    session_type.set("flashcard")

    session_alt_label = Label(main_frame, text="Select the calendar character type you would like to study:", padx=50)
    session_label = Label(main_frame, text="Select which session type you would like:", padx=50)

    flashcard = Radiobutton(main_frame, text="flashcards", variable=session_type, value="flashcard")
    test_session = Radiobutton(main_frame, text="test", variable=session_type, value="test")

    hiragana_button = Radiobutton(main_frame, text="hiragana", variable=session_type_alt, value="hiragana")
    kanji_button = Radiobutton(main_frame, text="kanji", variable=session_type_alt, value="kanji")

    session_alt_label.grid(row=0, column=0)
    hiragana_button.grid(row=1, column=0)
    kanji_button.grid(row=2, column=0)

    session_label.grid(row=0, column=1)
    flashcard.grid(row=1, column=1)
    test_session.grid(row=2, column=1)

    session_button = Button(main_frame, text="Create Session", command=calendar, pady=10)

    session_button.grid(row=3, column=0, columnspan=2)


def calendar():
    # This function runs the calendar window
    global main_frame
    global new_button
    global input_box
    global prompt
    global feedback
    global answer
    global show_button
    global enter

    for widget in main_frame.winfo_children():
        widget.destroy()

    input_box = Entry(main_frame, font=("Arial", 30), width=50)
    new_button = Button(main_frame, text="New Date", command=get_date)
    enter = Button(main_frame, text="Enter", command=test_date)
    if session_type.get() == "flashcard":
        enter["state"] = DISABLED
    prompt = Label(main_frame, text="Select the new date button to start practicing", font=("Arial", 15))
    feedback = Label(main_frame, text="Press the enter button to test your answer", font=("Arial", 15))
    show_button = Button(main_frame, text="Show Answer", command=show_date)
    answer = Label(main_frame, text="", font=("Arial", 15))
    Button(main_frame, text="main menu", font=("Arial", 15), command=main_menu).grid(row=0, column=3)

    input_box.grid(row=0, column=0, columnspan=3)
    new_button.grid(row=1, column=0)
    enter.grid(row=1, column=2)
    prompt.grid(row=2, column=0, columnspan=3)
    feedback.grid(row=3, column=0, columnspan=3)
    show_button.grid(row=1, column=1)


def get_date():
    # This function creates a random date for the calendar trainer
    global main_frame
    global new_button
    global prompt
    global feedback
    global month
    global day

    thirty_one = ["1", "3", "5", "7", "8", "10", "12"]
    thirty = ["4", "6", "9", "11"]

    month = str(random.randint(1, 12))
    if month in thirty_one:
        day = str(random.randint(1, 31))
    elif month in thirty:
        day = str(random.randint(1, 30))
    else:
        day = str(random.randint(1, 29))
    prompt_text = ""
    if session_type_alt.get() == "hiragana":
        prompt_text = "Enter the Hiragana for " + month + "/" + day
    if session_type_alt.get() == "kanji":
        prompt_text = "Enter the Hiragana for " + date_kanji(month, day)
    prompt.destroy()
    prompt = Label(main_frame, text=prompt_text, font=("Arial", 15))
    prompt.grid(row=2, column=0, columnspan=3)
    new_button["state"] = DISABLED
    show_button["state"] = NORMAL
    feedback.destroy()
    if session_type.get() == "flashcard":
        answer.destroy()


def test_date():
    # This function checks if the entry is correct for the calendar trainer
    global month
    global day
    global main_frame
    global input_box
    global new_button
    global feedback

    current_entry = input_box.get()
    if current_entry == date_convert():
        if feedback.winfo_exists() == 1:
            feedback.destroy()
        feedback = Label(main_frame, text="correct", font=("Arial", 15))
        feedback.grid(row=3, column=0, columnspan=3)
        input_box.delete(0, "end")
        new_button["state"] = NORMAL
    else:
        if feedback.winfo_exists() == 1:
            feedback.destroy()
        feedback = Label(main_frame, text="incorrect", font=("Arial", 15))
        feedback.grid(row=3, column=0, columnspan=3)


def show_date():
    # This function displays the current date
    global month
    global day
    global main_frame
    global answer
    global show_button

    answer = Label(main_frame, text=date_convert(), font=("Arial", 15))
    answer.grid(row=4, column=0, columnspan=3)
    show_button["state"] = DISABLED
    if session_type.get() == "flashcard":
        new_button["state"] = NORMAL


def date_convert():
    # This function converts an english date to a japanese date
    converted = ""

    exception_days = {"1": "ついたち",
                      "2": "ふつか",
                      "3": "みっか",
                      "4": "よっか",
                      "5": "いつか",
                      "6": "むいか",
                      "7": "なのか",
                      "8": "ようか",
                      "9": "ここのか",
                      "10": "とおか",
                      "14": "じゅうよっか",
                      "20": "はつか",
                      "24": "にじゅうよっか"}

    hir_num = {"1": "いち",
               "2": "に",
               "3": "さん",
               "5": "ご",
               "6": "ろく",
               "7": "しち",
               "8": "はち",
               "9": "く",
               "10": "じゅう",
               "11": "じゅういち",
               "12": "じゅうに"}

    if month in hir_num:
        converted += hir_num[month]
        converted += "がつ"
    else:
        converted += "しがつ"

    if day in exception_days:
        converted += exception_days[day]
    else:
        if day[0] == "1":
            converted += hir_num["10"]
        if day[0] == "2":
            converted += hir_num["2"]
            converted += hir_num["10"]
        if day[0] == "3":
            converted += hir_num["3"]
            converted += hir_num["10"]
        converted += hir_num[day[1]]
        converted += "にち"

    return converted


def date_kanji(cur_month, cur_day):
    # This function converts an english date to a japanese date
    converted = ""

    hir_num = {"1": "一",
               "2": "二",
               "3": "三",
               "4": "四",
               "5": "五",
               "6": "六",
               "7": "七",
               "8": "八",
               "9": "九",
               "10": "十",
               "11": "十一",
               "12": "十二",
               "0": ""}

    converted += hir_num[cur_month]
    converted += "月"

    if cur_day in hir_num:
        converted += hir_num[cur_day]
    else:
        if cur_day[0] == "1":
            converted += hir_num["10"]
            converted += hir_num[cur_day[1]]
        else:
            converted += hir_num[cur_day[0]]
            converted += hir_num["10"]
            converted += hir_num[cur_day[1]]

    converted += "日"

    return converted


def verb_menu():
    # This function runs a window where the user can customize their verb practice session

    global main_frame
    global session_type

    for widget in main_frame.winfo_children():
        widget.destroy()

    session_type = StringVar()
    session_type.set("flashcard")

    verb_label = Label(main_frame, text="Select the verb types you would like to study:", padx=50)
    unit_label = Label(main_frame, text="Select the units you would like to study:", padx=50)
    conj_label = Label(main_frame, text="Select the conjugations you would like to study:", padx=50)
    session_label = Label(main_frame, text="Select which session type you would like:", padx=50)

    verb_label.grid(row=0, column=1)
    unit_label.grid(row=0, column=0)
    conj_label.grid(row=0, column=2)

    ru = StringVar()
    u = StringVar()
    irr = StringVar()

    verb_types = [ru,
                  u,
                  irr]

    unit_1 = StringVar()
    unit_2 = StringVar()
    unit_3 = StringVar()
    unit_4 = StringVar()
    unit_5 = StringVar()
    unit_6 = StringVar()
    unit_7 = StringVar()
    unit_8 = StringVar()
    unit_9 = StringVar()
    unit_10 = StringVar()
    unit_11 = StringVar()
    unit_12 = StringVar()

    unit_list = [unit_1,
                 unit_2,
                 unit_3,
                 unit_4,
                 unit_5,
                 unit_6,
                 unit_7,
                 unit_8,
                 unit_9,
                 unit_10,
                 unit_11,
                 unit_12]

    pres_aff = StringVar()
    pres_neg = StringVar()
    past_aff = StringVar()
    past_neg = StringVar()
    te_form = StringVar()
    verb_stem = StringVar()
    short_past_aff = StringVar()
    short_past_neg = StringVar()
    short_pres_aff = StringVar()
    short_pres_neg = StringVar()

    conj_list = [pres_aff,
                 pres_neg,
                 past_aff,
                 past_neg,
                 te_form,
                 verb_stem,
                 short_past_aff,
                 short_past_neg,
                 short_pres_aff,
                 short_pres_neg]

    ru_check = Checkbutton(main_frame, text="ru", variable=ru, onvalue="ru", offvalue="")
    u_check = Checkbutton(main_frame, text="u", variable=u, onvalue="u", offvalue="")
    irr_check = Checkbutton(main_frame, text="irregular", variable=irr, onvalue="irregular", offvalue="")

    ru_check.grid(row=1, column=1)
    u_check.grid(row=2, column=1)
    irr_check.grid(row=3, column=1)

    unit_1_check = Checkbutton(main_frame, text="unit 1", variable=unit_1, onvalue="unit 1", offvalue="")
    unit_2_check = Checkbutton(main_frame, text="unit 2", variable=unit_2, onvalue="unit 2", offvalue="")
    unit_3_check = Checkbutton(main_frame, text="unit 3", variable=unit_3, onvalue="unit 3", offvalue="")
    unit_4_check = Checkbutton(main_frame, text="unit 4", variable=unit_4, onvalue="unit 4", offvalue="")
    unit_5_check = Checkbutton(main_frame, text="unit 5", variable=unit_5, onvalue="unit 5", offvalue="")
    unit_6_check = Checkbutton(main_frame, text="unit 6", variable=unit_6, onvalue="unit 6", offvalue="")
    unit_7_check = Checkbutton(main_frame, text="unit 7", variable=unit_7, onvalue="unit 7", offvalue="")
    unit_8_check = Checkbutton(main_frame, text="unit 8", variable=unit_8, onvalue="unit 8", offvalue="")
    unit_9_check = Checkbutton(main_frame, text="unit 9", variable=unit_9, onvalue="unit 9", offvalue="")
    unit_10_check = Checkbutton(main_frame, text="unit 10", variable=unit_10, onvalue="unit 10", offvalue="")
    unit_11_check = Checkbutton(main_frame, text="unit 11", variable=unit_11, onvalue="unit 11", offvalue="")
    unit_12_check = Checkbutton(main_frame, text="unit 12", variable=unit_12, onvalue="unit 12", offvalue="")

    unit_1_check.grid(row=1, column=0)
    unit_2_check.grid(row=2, column=0)
    unit_3_check.grid(row=3, column=0)
    unit_4_check.grid(row=4, column=0)
    unit_5_check.grid(row=5, column=0)
    unit_6_check.grid(row=6, column=0)
    unit_7_check.grid(row=7, column=0)
    unit_8_check.grid(row=8, column=0)
    unit_9_check.grid(row=9, column=0)
    unit_10_check.grid(row=10, column=0)
    unit_11_check.grid(row=11, column=0)
    unit_12_check.grid(row=12, column=0)

    unit_1_check.deselect()
    unit_2_check.deselect()
    unit_3_check.deselect()
    unit_4_check.deselect()
    unit_5_check.deselect()
    unit_6_check.deselect()
    unit_7_check.deselect()
    unit_8_check.deselect()
    unit_9_check.deselect()
    unit_10_check.deselect()
    unit_11_check.deselect()
    unit_12_check.deselect()

    pres_aff_check = Checkbutton(main_frame, text="present affirmative", variable=pres_aff,
                                 onvalue="present affirmative", offvalue="")
    pres_neg_check = Checkbutton(main_frame, text="present negative", variable=pres_neg,
                                 onvalue="present negative", offvalue="")
    past_aff_check = Checkbutton(main_frame, text="past affirmative", variable=past_aff,
                                 onvalue="past affirmative", offvalue="")
    past_neg_check = Checkbutton(main_frame, text="past negative", variable=past_neg,
                                 onvalue="past negative", offvalue="")
    te_form_check = Checkbutton(main_frame, text="te form", variable=te_form, onvalue="te form", offvalue="")
    short_pres_aff_check = Checkbutton(main_frame, text="short present affirmative", variable=short_pres_aff,
                                       onvalue="short present affirmative", offvalue="")
    short_pres_neg_check = Checkbutton(main_frame, text="short present negative", variable=short_pres_neg,
                                       onvalue="short present negative", offvalue="")
    short_past_aff_check = Checkbutton(main_frame, text="short past affirmative", variable=short_past_aff,
                                       onvalue="short past affirmative", offvalue="")
    short_past_neg_check = Checkbutton(main_frame, text="short past negative", variable=short_past_neg,
                                       onvalue="short past negative", offvalue="")
    verb_stem_check = Checkbutton(main_frame, text="verb stem", variable=verb_stem,
                                  onvalue="verb stem", offvalue="")

    pres_aff_check.grid(row=1, column=2)
    pres_neg_check.grid(row=2, column=2)
    past_aff_check.grid(row=3, column=2)
    past_neg_check.grid(row=4, column=2)
    te_form_check.grid(row=5, column=2)
    short_pres_aff_check.grid(row=6, column=2)
    short_pres_neg_check.grid(row=7, column=2)
    short_past_aff_check.grid(row=8, column=2)
    short_past_neg_check.grid(row=9, column=2)
    verb_stem_check.grid(row=10, column=2)

    pres_aff_check.deselect()
    pres_neg_check.deselect()
    past_aff_check.deselect()
    past_neg_check.deselect()
    te_form_check.deselect()
    short_pres_aff_check.deselect()
    short_pres_neg_check.deselect()
    short_past_aff_check.deselect()
    short_past_neg_check.deselect()
    verb_stem_check.deselect()

    flashcard = Radiobutton(main_frame, text="flashcards", variable=session_type, value="flashcard")
    test_session = Radiobutton(main_frame, text="test", variable=session_type, value="test")

    session_label.grid(row=0, column=3)
    flashcard.grid(row=1, column=3)
    test_session.grid(row=2, column=3)

    session_button = Button(main_frame, text="Create Session",
                            command=lambda: create_conj_session(unit_list, verb_types, conj_list), pady=10)

    session_button.grid(row=13, column=0, columnspan=3)


def create_conj_session(list_units, verb_list, conj_list):
    # This function creates a session by creating a session list and calling the conj session window function
    global main_frame
    global current

    session_list.clear()
    current = 0
    for unit in list_units:
        for verb_type in verb_list:
            if verb_type.get() != "":
                for i in range(len(vocab_list)):
                    if vocab_list[i].type == "verb" and \
                            vocab_list[i].category == verb_type.get() and vocab_list[i].unit == unit.get():
                        session_list.append(vocab_list[i])

    conjugations = []
    for c in conj_list:
        if c.get() != "":
            conjugations.append(c.get())

    shuffle_list(session_list)
    conj_session_window(conjugations)


def conj_session_window(conjugations):
    # This function runs the verb conjugation trainer session
    global main_frame
    global new_button
    global prompt
    global feedback
    global answer
    global show_button
    global enter
    global input_box
    global session_type

    for widget in main_frame.winfo_children():
        widget.destroy()

    new_button = Button(main_frame, text="New Verb", command=lambda: get_verb(conjugations))
    input_box = Entry(main_frame, font=("Arial", 30))
    enter = Button(main_frame, text="Enter", command=test_verb)
    if session_type.get() == "flashcard":
        enter["state"] = DISABLED
    prompt = Label(main_frame, text="Select the new verb button to start practicing", font=("Arial", 15))
    feedback = Label(main_frame, text="Press the enter button to test your answer", font=("Arial", 15))
    show_button = Button(main_frame, text="Show Answer", command=show_verb)
    answer = Label(main_frame, text="", font=("Arial", 15))
    Button(main_frame, text="main menu", font=("Arial", 15), command=main_menu).grid(row=0, column=3)

    new_button.grid(row=1, column=0)
    input_box.grid(row=0, column=0, columnspan=3)
    enter.grid(row=1, column=2)
    prompt.grid(row=2, column=0, columnspan=3)
    feedback.grid(row=3, column=0, columnspan=3)
    show_button.grid(row=1, column=1)


def get_verb(conjugations):
    # this function gets a verb from the session list and stores it in current and gets a conjugation type from
    # conjugations, and stores it in current_conj
    global current
    global main_frame
    global new_button
    global prompt
    global feedback
    global show_button
    global enter
    global current_conj

    current = random.randint(0, len(session_list) - 1)
    current_conj = conjugations[random.randint(0, len(conjugations) - 1)]
    prompt_text = "Enter the " + current_conj + " conjugation of " + session_list[current].english + ":"
    # A random word is selected from the session list
    prompt.destroy()
    prompt = Label(main_frame, text=prompt_text, font=("Arial", 15))
    prompt.grid(row=2, column=0, columnspan=3)
    # The old prompt is erased and the prompt for the new word is created and displayed
    new_button["state"] = DISABLED
    show_button["state"] = NORMAL
    if session_type.get() == "test":
        enter["state"] = NORMAL
    feedback.destroy()
    # The user is blocked from choosing a new word and the old feedback is removed to keep things running smooth
    if session_type.get() == "flashcard":
        answer.destroy()


def test_verb():
    # This function checks whether the correct answer was entered
    global main_frame
    global input_box
    global new_button
    global feedback
    global answer
    global show_button
    global enter

    current_entry = input_box.get()
    if current_entry == conjugate_verb(current, current_conj):
        if feedback.winfo_exists() == 1:
            feedback.destroy()
        if answer.winfo_exists() == 1:
            answer.destroy()
        feedback = Label(main_frame, text="correct", font=("Arial", 15))
        feedback.grid(row=3, column=0, columnspan=3)
        input_box.delete(0, "end")
        new_button["state"] = NORMAL
        enter["state"] = DISABLED
    else:
        if feedback.winfo_exists() == 1:
            feedback.destroy()
        feedback = Label(main_frame, text="incorrect", font=("Arial", 15))
        feedback.grid(row=3, column=0, columnspan=3)


def show_verb():
    # This function displays the current verb in conjugated form
    global main_frame
    global answer
    global show_button

    answer = Label(main_frame, text=conjugate_verb(current, current_conj), font=("Arial", 15))
    answer.grid(row=4, column=0, columnspan=3)
    show_button["state"] = DISABLED
    if session_type.get() == "flashcard":
        new_button["state"] = NORMAL


def conjugate_verb(curr, curr_conj):
    conj_verb = session_list[curr].japanese

    if curr_conj == "present affirmative":
        if session_list[curr].category == "ru":
            conj_verb = conj_verb[:len(conj_verb) - 1]
            conj_verb += "ます"

        if session_list[curr].category == "u":
            conj_verb = conj_verb[:len(conj_verb) - 1]
            conj_verb += session_list[curr].subject
            conj_verb += "ます"

        if session_list[curr].category == "irregular":
            conj_verb = conj_verb[:len(conj_verb) - 2]
            if session_list[curr].subject == "する":
                conj_verb += "します"
            if session_list[curr].subject == "くる":
                conj_verb += "きます"

    if curr_conj == "present negative":
        if session_list[curr].category == "ru":
            conj_verb = conj_verb[:len(conj_verb) - 1]
            conj_verb += "ません"

        if session_list[curr].category == "u":
            conj_verb = conj_verb[:len(conj_verb) - 1]
            conj_verb += session_list[curr].subject
            conj_verb += "ません"

        if session_list[curr].category == "irregular":
            conj_verb = conj_verb[:len(conj_verb) - 2]
            if session_list[curr].subject == "する":
                conj_verb += "しません"
            if session_list[curr].subject == "くる":
                conj_verb += "きません"

    if curr_conj == "past affirmative":
        if session_list[curr].category == "ru":
            conj_verb = conj_verb[:len(conj_verb) - 1]
            conj_verb += "ました"

        if session_list[curr].category == "u":
            conj_verb = conj_verb[:len(conj_verb) - 1]
            conj_verb += session_list[current].subject
            conj_verb += "ました"

        if session_list[curr].category == "irregular":
            conj_verb = conj_verb[:len(conj_verb) - 2]
            if session_list[curr].subject == "する":
                conj_verb += "しました"
            if session_list[curr].subject == "くる":
                conj_verb += "きました"

    if curr_conj == "past negative":
        if session_list[curr].category == "ru":
            conj_verb = conj_verb[:len(conj_verb) - 1]
            conj_verb += "ませんでした"

        if session_list[curr].category == "u":
            conj_verb = conj_verb[:len(conj_verb) - 1]
            conj_verb += session_list[curr].subject
            conj_verb += "ませんでした"

        if session_list[curr].category == "irregular":
            conj_verb = conj_verb[:len(conj_verb) - 2]
            if session_list[curr].subject == "する":
                conj_verb += "しませんでした"
            if session_list[curr].subject == "くる":
                conj_verb += "きませんでした"

    if curr_conj == "te form":
        if session_list[curr].category == "ru":
            conj_verb = conj_verb[:len(conj_verb) - 1]
            conj_verb += "て"

        if session_list[curr].category == "u":
            conj_verb = conj_verb[:len(conj_verb) - 1]
            if (session_list[curr].subject == "い" or session_list[curr].subject == "ち"
                    or session_list[curr].subject == "り"):
                conj_verb += "って"

            if (session_list[curr].subject == "み" or session_list[curr].subject == "び"
                    or session_list[curr].subject == "に"):
                conj_verb += "んで"

            if session_list[curr].subject == "ぎ":
                conj_verb += "いで"

            if session_list[curr].subject == "し":
                conj_verb += "して"

            if session_list[curr].subject == "き":
                if session_list[curr].japanese == "いく":
                    conj_verb += "って"
                else:
                    conj_verb += "いて"

        if session_list[curr].category == "irregular":
            conj_verb = conj_verb[:len(conj_verb) - 2]
            if session_list[curr].subject == "する":
                conj_verb += "して"
            if session_list[curr].subject == "くる":
                conj_verb += "きて"

    if curr_conj == "verb stem":
        if session_list[curr].category == "ru":
            conj_verb = conj_verb[:len(conj_verb) - 1]

        if session_list[curr].category == "u":
            conj_verb = conj_verb[:len(conj_verb) - 1]
            conj_verb += session_list[curr].subject

        if session_list[curr].category == "irregular":
            conj_verb = conj_verb[:len(conj_verb) - 2]
            if session_list[curr].subject == "する":
                conj_verb += "し"
            if session_list[curr].subject == "くる":
                conj_verb += "き"

    if curr_conj == "short present affirmative":
        pass

    if curr_conj == "short present negative":
        if session_list[curr].category == "ru":
            conj_verb = conj_verb[:len(conj_verb) - 1]
            conj_verb += "ない"

        if session_list[current].category == "u" and session_list[curr].japanese != "ある":
            conj_verb = conj_verb[:len(conj_verb) - 1]
            if session_list[curr].subject == "い":
                conj_verb += "わない"
            if session_list[curr].subject == "き":
                conj_verb += "かない"
            if session_list[curr].subject == "り":
                conj_verb += "らない"
            if session_list[curr].subject == "み":
                conj_verb += "まない"
            if session_list[curr].subject == "に":
                conj_verb += "なない"
            if session_list[curr].subject == "し":
                conj_verb += "さない"
            if session_list[curr].subject == "ち":
                conj_verb += "わたない"
            if session_list[curr].subject == "び":
                conj_verb += "ばない"
            if session_list[curr].subject == "ぎ":
                conj_verb += "がない"

        if session_list[curr].category == "irregular":
            conj_verb = conj_verb[:len(conj_verb) - 2]
            if session_list[curr].subject == "する":
                conj_verb += "しない"
            if session_list[curr].subject == "くる":
                conj_verb += "こない"

        if session_list[curr].japanese == "ある":
            conj_verb = "ない"

    if curr_conj == "short past affirmative":
        te = conjugate_verb(current, "te form")

        if te[len(te) - 1] == "て":
            te = te[:len(te) - 1]
            te += "た"

        elif te[len(te) - 1] == "で":
            te = te[:len(te) - 1]
            te += "だ"

        conj_verb = te

    if curr_conj == "short past negative":
        nai = conjugate_verb(current, "short present negative")

        nai = nai[:len(nai) - 1]
        nai += "かった"

        conj_verb = nai

    return conj_verb


def adjective_menu():
    # This function runs a window where the user can customize their adjective practice session

    global main_frame
    global session_type

    for widget in main_frame.winfo_children():
        widget.destroy()

    session_type = StringVar()
    session_type.set("flashcard")

    verb_label = Label(main_frame, text="Select the adjective types you would like to study:", padx=50)
    unit_label = Label(main_frame, text="Select the units you would like to study:", padx=50)
    conj_label = Label(main_frame, text="Select the conjugations you would like to study:", padx=50)
    session_label = Label(main_frame, text="Select which session type you would like:", padx=50)

    verb_label.grid(row=0, column=1)
    unit_label.grid(row=0, column=0)
    conj_label.grid(row=0, column=2)

    i = StringVar()
    na = StringVar()
    irr = StringVar()

    adj_types = [i,
                 na,
                 irr]

    unit_1 = StringVar()
    unit_2 = StringVar()
    unit_3 = StringVar()
    unit_4 = StringVar()
    unit_5 = StringVar()
    unit_6 = StringVar()
    unit_7 = StringVar()
    unit_8 = StringVar()
    unit_9 = StringVar()
    unit_10 = StringVar()
    unit_11 = StringVar()
    unit_12 = StringVar()
    bonus_1 = StringVar()

    unit_list = [unit_1,
                 unit_2,
                 unit_3,
                 unit_4,
                 unit_5,
                 unit_6,
                 unit_7,
                 unit_8,
                 unit_9,
                 unit_10,
                 unit_11,
                 unit_12,
                 bonus_1]

    pres_aff = StringVar()
    pres_neg = StringVar()
    past_aff = StringVar()
    past_neg = StringVar()
    short_past_aff = StringVar()
    short_past_neg = StringVar()
    short_pres_aff = StringVar()
    short_pres_neg = StringVar()

    conj_list = [pres_aff,
                 pres_neg,
                 past_aff,
                 past_neg,
                 short_past_aff,
                 short_past_neg,
                 short_pres_aff,
                 short_pres_neg]

    i_check = Checkbutton(main_frame, text="i", variable=i, onvalue="i", offvalue="")
    na_check = Checkbutton(main_frame, text="na", variable=na, onvalue="na", offvalue="")
    irr_check = Checkbutton(main_frame, text="irregular", variable=irr, onvalue="irregular", offvalue="")

    i_check.grid(row=1, column=1)
    na_check.grid(row=2, column=1)
    irr_check.grid(row=3, column=1)

    unit_1_check = Checkbutton(main_frame, text="unit 1", variable=unit_1, onvalue="unit 1", offvalue="")
    unit_2_check = Checkbutton(main_frame, text="unit 2", variable=unit_2, onvalue="unit 2", offvalue="")
    unit_3_check = Checkbutton(main_frame, text="unit 3", variable=unit_3, onvalue="unit 3", offvalue="")
    unit_4_check = Checkbutton(main_frame, text="unit 4", variable=unit_4, onvalue="unit 4", offvalue="")
    unit_5_check = Checkbutton(main_frame, text="unit 5", variable=unit_5, onvalue="unit 5", offvalue="")
    unit_6_check = Checkbutton(main_frame, text="unit 6", variable=unit_6, onvalue="unit 6", offvalue="")
    unit_7_check = Checkbutton(main_frame, text="unit 7", variable=unit_7, onvalue="unit 7", offvalue="")
    unit_8_check = Checkbutton(main_frame, text="unit 8", variable=unit_8, onvalue="unit 8", offvalue="")
    unit_9_check = Checkbutton(main_frame, text="unit 9", variable=unit_9, onvalue="unit 9", offvalue="")
    unit_10_check = Checkbutton(main_frame, text="unit 10", variable=unit_10, onvalue="unit 10", offvalue="")
    unit_11_check = Checkbutton(main_frame, text="unit 11", variable=unit_11, onvalue="unit 11", offvalue="")
    unit_12_check = Checkbutton(main_frame, text="unit 12", variable=unit_12, onvalue="unit 12", offvalue="")
    bonus_1_check = Checkbutton(main_frame, text="bonus 1", variable=bonus_1, onvalue="bonus 1", offvalue="")

    unit_1_check.grid(row=1, column=0)
    unit_2_check.grid(row=2, column=0)
    unit_3_check.grid(row=3, column=0)
    unit_4_check.grid(row=4, column=0)
    unit_5_check.grid(row=5, column=0)
    unit_6_check.grid(row=6, column=0)
    unit_7_check.grid(row=7, column=0)
    unit_8_check.grid(row=8, column=0)
    unit_9_check.grid(row=9, column=0)
    unit_10_check.grid(row=10, column=0)
    unit_11_check.grid(row=11, column=0)
    unit_12_check.grid(row=12, column=0)
    bonus_1_check.grid(row=13, column=0)

    unit_1_check.deselect()
    unit_2_check.deselect()
    unit_3_check.deselect()
    unit_4_check.deselect()
    unit_5_check.deselect()
    unit_6_check.deselect()
    unit_7_check.deselect()
    unit_8_check.deselect()
    unit_9_check.deselect()
    unit_10_check.deselect()
    unit_11_check.deselect()
    unit_12_check.deselect()
    bonus_1_check.deselect()

    pres_aff_check = Checkbutton(main_frame, text="present affirmative", variable=pres_aff,
                                 onvalue="present affirmative", offvalue="")
    pres_neg_check = Checkbutton(main_frame, text="present negative", variable=pres_neg,
                                 onvalue="present negative", offvalue="")
    past_aff_check = Checkbutton(main_frame, text="past affirmative", variable=past_aff,
                                 onvalue="past affirmative", offvalue="")
    past_neg_check = Checkbutton(main_frame, text="past negative", variable=past_neg,
                                 onvalue="past negative", offvalue="")
    short_pres_aff_check = Checkbutton(main_frame, text="short present affirmative", variable=short_pres_aff,
                                       onvalue="short present affirmative", offvalue="")
    short_pres_neg_check = Checkbutton(main_frame, text="short present negative", variable=short_pres_neg,
                                       onvalue="short present negative", offvalue="")
    short_past_aff_check = Checkbutton(main_frame, text="short past affirmative", variable=short_past_aff,
                                       onvalue="short past affirmative", offvalue="")
    short_past_neg_check = Checkbutton(main_frame, text="short past negative", variable=short_past_neg,
                                       onvalue="short past negative", offvalue="")

    pres_aff_check.grid(row=1, column=2)
    pres_neg_check.grid(row=2, column=2)
    past_aff_check.grid(row=3, column=2)
    past_neg_check.grid(row=4, column=2)
    short_pres_aff_check.grid(row=5, column=2)
    short_pres_neg_check.grid(row=6, column=2)
    short_past_aff_check.grid(row=7, column=2)
    short_past_neg_check.grid(row=8, column=2)

    pres_aff_check.deselect()
    pres_neg_check.deselect()
    past_aff_check.deselect()
    past_neg_check.deselect()
    short_pres_aff_check.deselect()
    short_pres_neg_check.deselect()
    short_past_aff_check.deselect()
    short_past_neg_check.deselect()

    flashcard = Radiobutton(main_frame, text="flashcards", variable=session_type, value="flashcard")
    test_session = Radiobutton(main_frame, text="test", variable=session_type, value="test")

    session_label.grid(row=0, column=3)
    flashcard.grid(row=1, column=3)
    test_session.grid(row=2, column=3)

    session_button = Button(main_frame, text="Create Session",
                            command=lambda: create_adj_session(unit_list, adj_types, conj_list), pady=10)

    session_button.grid(row=14, column=0, columnspan=3)


def create_adj_session(list_units, adj_list, conj_list):
    # This function creates a session by creating a session list and calling the adj session window function
    global main_frame
    global current

    session_list.clear()
    current = 0
    for unit in list_units:
        for adj_type in adj_list:
            if adj_type.get() != "":
                for i in range(len(vocab_list)):
                    if vocab_list[i].type == "adjective" and \
                            vocab_list[i].category == adj_type.get() and vocab_list[i].unit == unit.get():
                        session_list.append(vocab_list[i])

    conjugations = []
    for c in conj_list:
        if c.get() != "":
            conjugations.append(c.get())

    shuffle_list(session_list)
    adj_session_window(conjugations)


def adj_session_window(conjugations):
    # This function runs the adjective conjugation trainer session
    global main_frame
    global new_button
    global prompt
    global feedback
    global answer
    global show_button
    global enter
    global input_box

    for widget in main_frame.winfo_children():
        widget.destroy()

    new_button = Button(main_frame, text="New Adjective", command=lambda: get_adj(conjugations))
    input_box = Entry(main_frame, font=("Arial", 30))
    enter = Button(main_frame, text="Enter", command=test_adj)
    if session_type.get() == "flashcard":
        enter["state"] = DISABLED
    prompt = Label(main_frame, text="Select the new adjective button to start practicing", font=("Arial", 15))
    feedback = Label(main_frame, text="Press the enter button to test your answer", font=("Arial", 15))
    show_button = Button(main_frame, text="Show Answer", command=show_adj)
    answer = Label(main_frame, text="", font=("Arial", 15))
    Button(main_frame, text="main menu", font=("Arial", 15), command=main_menu).grid(row=0, column=3)

    new_button.grid(row=1, column=0)
    input_box.grid(row=0, column=0, columnspan=3)
    enter.grid(row=1, column=2)
    prompt.grid(row=2, column=0, columnspan=3)
    feedback.grid(row=3, column=0, columnspan=3)
    show_button.grid(row=1, column=1)


def get_adj(conjugations):
    # this function gets an adjective from the session list and stores it in current and gets a conjugation type from
    # conjugations, and stores it in current_conj
    global current
    global main_frame
    global new_button
    global prompt
    global feedback
    global show_button
    global enter
    global current_conj

    current = random.randint(0, len(session_list) - 1)
    current_conj = conjugations[random.randint(0, len(conjugations) - 1)]
    prompt_text = "Enter the " + current_conj + " conjugation of " + session_list[current].english + ":"
    # A random word is selected from the session list
    prompt.destroy()
    prompt = Label(main_frame, text=prompt_text, font=("Arial", 15))
    prompt.grid(row=2, column=0, columnspan=3)
    # The old prompt is erased and the prompt for the new word is created and displayed
    new_button["state"] = DISABLED
    show_button["state"] = NORMAL
    if session_type.get() == "test":
        enter["state"] = NORMAL
    feedback.destroy()
    # The user is blocked from choosing a new word and the old feedback is removed to keep things running smooth
    if session_type.get() == "flashcard":
        answer.destroy()


def test_adj():
    # This function checks whether the correct answer was entered
    global main_frame
    global input_box
    global new_button
    global feedback
    global answer
    global show_button
    global enter

    current_entry = input_box.get()
    if current_entry == conjugate_adj():
        if feedback.winfo_exists() == 1:
            feedback.destroy()
        if answer.winfo_exists() == 1:
            answer.destroy()
        feedback = Label(main_frame, text="correct", font=("Arial", 15))
        feedback.grid(row=3, column=0, columnspan=3)
        input_box.delete(0, "end")
        new_button["state"] = NORMAL
        enter["state"] = DISABLED
    else:
        if feedback.winfo_exists() == 1:
            feedback.destroy()
        feedback = Label(main_frame, text="incorrect", font=("Arial", 15))
        feedback.grid(row=3, column=0, columnspan=3)


def show_adj():
    # This function displays the current verb in conjugated form
    global main_frame
    global answer
    global show_button

    answer = Label(main_frame, text=conjugate_adj(), font=("Arial", 15))
    answer.grid(row=4, column=0, columnspan=3)
    show_button["state"] = DISABLED
    if session_type.get() == "flashcard":
        new_button["state"] = NORMAL


def conjugate_adj():
    global current
    global current_conj
    conj_adj = session_list[current].japanese

    if current_conj == "present affirmative":
        if session_list[current].category == "i":
            conj_adj += "です"

        if session_list[current].category == "na":
            conj_adj = conj_adj[:len(conj_adj) - 1]
            conj_adj += "です"

        if session_list[current].category == "irregular":
            conj_adj += "です"

    if current_conj == "present negative":
        if session_list[current].category == "i":
            conj_adj = conj_adj[:len(conj_adj) - 1]
            conj_adj += "くないです"

        if session_list[current].category == "na":
            conj_adj = conj_adj[:len(conj_adj) - 1]
            conj_adj += "じゃないです"

        if session_list[current].category == "irregular":
            conj_adj = conj_adj[:len(conj_adj) - 2]
            conj_adj += "よくないです"

    if current_conj == "past affirmative":
        if session_list[current].category == "i":
            conj_adj = conj_adj[:len(conj_adj) - 1]
            conj_adj += "かったです"

        if session_list[current].category == "na":
            conj_adj = conj_adj[:len(conj_adj) - 1]
            conj_adj += "でした"

        if session_list[current].category == "irregular":
            conj_adj = conj_adj[:len(conj_adj) - 2]
            conj_adj += "よかったです"

    if current_conj == "past negative":
        if session_list[current].category == "i":
            conj_adj = conj_adj[:len(conj_adj) - 1]
            conj_adj += "くなかったです"

        if session_list[current].category == "na":
            conj_adj = conj_adj[:len(conj_adj) - 1]
            conj_adj += "じゃなかったです"

        if session_list[current].category == "irregular":
            conj_adj = conj_adj[:len(conj_adj) - 2]
            conj_adj += "よくなかったです"

    if current_conj == "short present affirmative":
        if session_list[current].category == "i":
            pass

        if session_list[current].category == "na":
            conj_adj = conj_adj[:len(conj_adj) - 1]
            conj_adj += "だ"

        if session_list[current].category == "irregular":
            pass

    if current_conj == "short present negative":
        if session_list[current].category == "i":
            conj_adj = conj_adj[:len(conj_adj) - 1]
            conj_adj += "くない"

        if session_list[current].category == "na":
            conj_adj = conj_adj[:len(conj_adj) - 1]
            conj_adj += "じゃない"

        if session_list[current].category == "irregular":
            conj_adj = conj_adj[:len(conj_adj) - 2]
            conj_adj += "よくない"

    if current_conj == "short past affirmative":
        if session_list[current].category == "i":
            conj_adj = conj_adj[:len(conj_adj) - 1]
            conj_adj += "かった"

        if session_list[current].category == "na":
            conj_adj = conj_adj[:len(conj_adj) - 1]
            conj_adj += "だった"

        if session_list[current].category == "irregular":
            conj_adj = conj_adj[:len(conj_adj) - 2]
            conj_adj += "よかった"

    if current_conj == "short past negative":
        if session_list[current].category == "i":
            conj_adj = conj_adj[:len(conj_adj) - 1]
            conj_adj += "くなかった"

        if session_list[current].category == "na":
            conj_adj = conj_adj[:len(conj_adj) - 1]
            conj_adj += "じゃなかった"

        if session_list[current].category == "irregular":
            conj_adj = conj_adj[:len(conj_adj) - 2]
            conj_adj += "よくなかった"

    return conj_adj


def kanji_menu():
    # This function creates the menu that allows user to customize their kanji session
    global main_frame
    global session_type

    for widget in main_frame.winfo_children():
        widget.destroy()

    unit_1 = StringVar()
    unit_2 = StringVar()
    unit_3 = StringVar()
    unit_4 = StringVar()
    unit_5 = StringVar()
    unit_6 = StringVar()
    unit_7 = StringVar()
    unit_8 = StringVar()
    unit_9 = StringVar()
    unit_10 = StringVar()
    unit_11 = StringVar()
    unit_12 = StringVar()
    bonus_1 = StringVar()
    session_type = StringVar()
    session_type.set("flashcard")

    unit_list = [unit_1,
                 unit_2,
                 unit_3,
                 unit_4,
                 unit_5,
                 unit_6,
                 unit_7,
                 unit_8,
                 unit_9,
                 unit_10,
                 unit_11,
                 unit_12,
                 bonus_1]

    unit_label = Label(main_frame, text="Select the units you would like to study:", padx=50)
    session_label = Label(main_frame, text="Select which session type you would like:", padx=50)

    unit_1_check = Checkbutton(main_frame, text="unit 1", variable=unit_1, onvalue="unit 1", offvalue="")
    unit_2_check = Checkbutton(main_frame, text="unit 2", variable=unit_2, onvalue="unit 2", offvalue="")
    unit_3_check = Checkbutton(main_frame, text="unit 3", variable=unit_3, onvalue="unit 3", offvalue="")
    unit_4_check = Checkbutton(main_frame, text="unit 4", variable=unit_4, onvalue="unit 4", offvalue="")
    unit_5_check = Checkbutton(main_frame, text="unit 5", variable=unit_5, onvalue="unit 5", offvalue="")
    unit_6_check = Checkbutton(main_frame, text="unit 6", variable=unit_6, onvalue="unit 6", offvalue="")
    unit_7_check = Checkbutton(main_frame, text="unit 7", variable=unit_7, onvalue="unit 7", offvalue="")
    unit_8_check = Checkbutton(main_frame, text="unit 8", variable=unit_8, onvalue="unit 8", offvalue="")
    unit_9_check = Checkbutton(main_frame, text="unit 9", variable=unit_9, onvalue="unit 9", offvalue="")
    unit_10_check = Checkbutton(main_frame, text="unit 10", variable=unit_10, onvalue="unit 10", offvalue="")
    unit_11_check = Checkbutton(main_frame, text="unit 11", variable=unit_11, onvalue="unit 11", offvalue="")
    unit_12_check = Checkbutton(main_frame, text="unit 12", variable=unit_12, onvalue="unit 12", offvalue="")
    bonus_1_check = Checkbutton(main_frame, text="bonus 1", variable=bonus_1, onvalue="bonus 1", offvalue="")

    unit_label.grid(row=0, column=0)
    unit_1_check.grid(row=1, column=0)
    unit_2_check.grid(row=2, column=0)
    unit_3_check.grid(row=3, column=0)
    unit_4_check.grid(row=4, column=0)
    unit_5_check.grid(row=5, column=0)
    unit_6_check.grid(row=6, column=0)
    unit_7_check.grid(row=7, column=0)
    unit_8_check.grid(row=8, column=0)
    unit_9_check.grid(row=9, column=0)
    unit_10_check.grid(row=10, column=0)
    unit_11_check.grid(row=11, column=0)
    unit_12_check.grid(row=12, column=0)
    bonus_1_check.grid(row=13, column=0)

    unit_1_check.deselect()
    unit_2_check.deselect()
    unit_3_check.deselect()
    unit_4_check.deselect()
    unit_5_check.deselect()
    unit_6_check.deselect()
    unit_7_check.deselect()
    unit_8_check.deselect()
    unit_9_check.deselect()
    unit_10_check.deselect()
    unit_11_check.deselect()
    unit_12_check.deselect()
    bonus_1_check.deselect()

    flashcard = Radiobutton(main_frame, text="flashcards", variable=session_type, value="flashcard")
    test_session = Radiobutton(main_frame, text="test", variable=session_type, value="test")
    session_label.grid(row=0, column=1)
    flashcard.grid(row=1, column=1)
    test_session.grid(row=2, column=1)

    session_button = Button(main_frame, text="Create Session", command=lambda: create_kanji_session(unit_list), pady=10)

    session_button.grid(row=14, column=0, columnspan=1)


def create_kanji_session(unit_list):
    # This function creates a session by creating a session list and calling the kanji session window function
    global main_frame
    global current

    session_list.clear()
    current = 0
    for unit in unit_list:
        for i in range(len(vocab_list)):
            if vocab_list[i].kanji != "" and vocab_list[i].unit == unit.get():
                session_list.append(vocab_list[i])

    shuffle_list(session_list)
    kanji_session_window()


def kanji_session_window():
    # This function runs the kanji trainer session
    global main_frame
    global new_button
    global prompt
    global feedback
    global answer
    global show_button
    global enter
    global input_box
    global session_type

    for widget in main_frame.winfo_children():
        widget.destroy()

    new_button = Button(main_frame, text="New Kanji", command=get_kanji)
    input_box = Entry(main_frame, font=("Arial", 30))
    enter = Button(main_frame, text="Enter", command=test_kanji)
    if session_type.get() == "flashcard":
        enter["state"] = DISABLED
    prompt = Label(main_frame, text="Select the new kanji button to start practicing", font=("Arial", 15))
    feedback = Label(main_frame, text="Press the enter button to test your answer", font=("Arial", 15))
    show_button = Button(main_frame, text="Show Answer", command=show_kanji)
    answer = Label(main_frame, text="", font=("Arial", 15))
    Button(main_frame, text="main menu", font=("Arial", 15), command=main_menu).grid(row=0, column=3)

    new_button.grid(row=1, column=0)
    input_box.grid(row=0, column=0, columnspan=3)
    enter.grid(row=1, column=2)
    prompt.grid(row=2, column=0, columnspan=3)
    feedback.grid(row=3, column=0, columnspan=3)
    show_button.grid(row=1, column=1)


def get_kanji():
    # this function gets a kanji from the session list and stores it in current word
    global current
    global main_frame
    global new_button
    global prompt
    global feedback
    global show_button
    global enter
    global session_type

    counter = len(session_list)
    current = (current + 1) % len(session_list)
    # This loop ensures that users will only receive kanji that have not been correctly identified
    # 3 times in a row
    while session_list[current].num_correct > 2 and counter > 0:
        current = (current + 1) % len(session_list)
        counter -= 1
    # if all kanji in the session list have been identified correctly 3 times in a row, they are all reset
    if counter == 0:
        for i in range(len(session_list)):
            session_list[i].num_correct = 0
            session_list[current].first_attempt = True
        end_message = "Session complete, you may keep studying or exit to start new session"
        end_label = Label(main_frame, text=end_message, font=("Arial", 15))
        end_label.grid(row=4, column=0, columnspan=3)
    prompt_text = "Enter the Hiragana word for " + session_list[current].kanji + ":"
    prompt.destroy()
    prompt = Label(main_frame, text=prompt_text, font=("Arial", 15))
    prompt.grid(row=2, column=0, columnspan=3)
    # The old prompt is erased and the prompt for the new kanji is created and displayed
    new_button["state"] = DISABLED
    show_button["state"] = NORMAL
    if session_type.get() == "test":
        enter["state"] = NORMAL
    feedback.destroy()
    # The user is blocked from choosing a new kanji and the old feedback is removed to keep things running smooth
    if session_type.get() == "flashcard":
        answer.destroy()


def test_kanji():
    # This function checks whether the correct answer was entered
    global main_frame
    global input_box
    global new_button
    global feedback
    global answer
    global show_button
    global enter

    current_entry = input_box.get()
    if current_entry == session_list[current].japanese:
        if session_list[current].first_attempt:
            session_list[current].num_correct = 3
        session_list[current].num_correct += 1
        if feedback.winfo_exists() == 1:
            feedback.destroy()
        if answer.winfo_exists() == 1:
            answer.destroy()
        feedback = Label(main_frame, text="correct", font=("Arial", 15))
        feedback.grid(row=3, column=0, columnspan=3)
        input_box.delete(0, "end")
        new_button["state"] = NORMAL
        enter["state"] = DISABLED
    else:
        session_list[current].num_correct = 0
        if session_list[current].first_attempt:
            session_list[current].first_attempt = False
        if feedback.winfo_exists() == 1:
            feedback.destroy()
        feedback = Label(main_frame, text="incorrect", font=("Arial", 15))
        feedback.grid(row=3, column=0, columnspan=3)


def show_kanji():
    # This function displays the current kanji
    global main_frame
    global current
    global answer
    global show_button

    session_list[current].num_correct = 0
    if session_list[current].first_attempt:
        session_list[current].first_attempt = False
    answer = Label(main_frame, text=session_list[current].japanese, font=("Arial", 15))
    answer.grid(row=4, column=0, columnspan=3)
    show_button["state"] = DISABLED
    if session_type.get() == "flashcard":
        new_button["state"] = NORMAL


def kanji_w_menu():
    # This function creates the menu that allows user to customize their kanji writing session
    global main_frame

    for widget in main_frame.winfo_children():
        widget.destroy()

    unit_1 = StringVar()
    unit_2 = StringVar()
    unit_3 = StringVar()
    unit_4 = StringVar()
    unit_5 = StringVar()
    unit_6 = StringVar()
    unit_7 = StringVar()
    unit_8 = StringVar()
    unit_9 = StringVar()
    unit_10 = StringVar()
    unit_11 = StringVar()
    unit_12 = StringVar()
    bonus_1 = StringVar()

    unit_list = [unit_1,
                 unit_2,
                 unit_3,
                 unit_4,
                 unit_5,
                 unit_6,
                 unit_7,
                 unit_8,
                 unit_9,
                 unit_10,
                 unit_11,
                 unit_12,
                 bonus_1]

    unit_label = Label(main_frame, text="Select the units you would like to study:", padx=50)

    unit_1_check = Checkbutton(main_frame, text="unit 1", variable=unit_1, onvalue="unit 1", offvalue="")
    unit_2_check = Checkbutton(main_frame, text="unit 2", variable=unit_2, onvalue="unit 2", offvalue="")
    unit_3_check = Checkbutton(main_frame, text="unit 3", variable=unit_3, onvalue="unit 3", offvalue="")
    unit_4_check = Checkbutton(main_frame, text="unit 4", variable=unit_4, onvalue="unit 4", offvalue="")
    unit_5_check = Checkbutton(main_frame, text="unit 5", variable=unit_5, onvalue="unit 5", offvalue="")
    unit_6_check = Checkbutton(main_frame, text="unit 6", variable=unit_6, onvalue="unit 6", offvalue="")
    unit_7_check = Checkbutton(main_frame, text="unit 7", variable=unit_7, onvalue="unit 7", offvalue="")
    unit_8_check = Checkbutton(main_frame, text="unit 8", variable=unit_8, onvalue="unit 8", offvalue="")
    unit_9_check = Checkbutton(main_frame, text="unit 9", variable=unit_9, onvalue="unit 9", offvalue="")
    unit_10_check = Checkbutton(main_frame, text="unit 10", variable=unit_10, onvalue="unit 10", offvalue="")
    unit_11_check = Checkbutton(main_frame, text="unit 11", variable=unit_11, onvalue="unit 11", offvalue="")
    unit_12_check = Checkbutton(main_frame, text="unit 12", variable=unit_12, onvalue="unit 12", offvalue="")
    bonus_1_check = Checkbutton(main_frame, text="bonus 1", variable=bonus_1, onvalue="bonus 1", offvalue="")

    unit_label.grid(row=0, column=0)
    unit_1_check.grid(row=1, column=0)
    unit_2_check.grid(row=2, column=0)
    unit_3_check.grid(row=3, column=0)
    unit_4_check.grid(row=4, column=0)
    unit_5_check.grid(row=5, column=0)
    unit_6_check.grid(row=6, column=0)
    unit_7_check.grid(row=7, column=0)
    unit_8_check.grid(row=8, column=0)
    unit_9_check.grid(row=9, column=0)
    unit_10_check.grid(row=10, column=0)
    unit_11_check.grid(row=11, column=0)
    unit_12_check.grid(row=12, column=0)
    bonus_1_check.grid(row=13, column=0)

    unit_1_check.deselect()
    unit_2_check.deselect()
    unit_3_check.deselect()
    unit_4_check.deselect()
    unit_5_check.deselect()
    unit_6_check.deselect()
    unit_7_check.deselect()
    unit_8_check.deselect()
    unit_9_check.deselect()
    unit_10_check.deselect()
    unit_11_check.deselect()
    unit_12_check.deselect()
    bonus_1_check.deselect()

    session_button = Button(main_frame, text="Create Session",
                            command=lambda: create_kanji_w_session(unit_list), pady=10)

    session_button.grid(row=14, column=0, columnspan=1)


def create_kanji_w_session(unit_list):
    # This function creates a session by creating a session list and calling the kanji writing session window function
    global main_frame
    global current

    session_list.clear()
    current = 0
    for unit in unit_list:
        for i in range(len(vocab_list)):
            if vocab_list[i].kanji != "" and vocab_list[i].unit == unit.get():
                session_list.append(vocab_list[i])

    shuffle_list(session_list)
    kanji_w_session_window()


def kanji_w_session_window():
    # This function runs the kanji writing trainer session
    global main_frame
    global new_button
    global prompt
    global feedback
    global show_button

    for widget in main_frame.winfo_children():
        widget.destroy()

    new_button = Button(main_frame, text="New Kanji", command=get_kanji_w)
    prompt = Label(main_frame, text="Select the new kanji button to start practicing", font=("Arial", 15))
    feedback = Label(main_frame, text="Press the show kanji button to reveal the character", font=("Arial", 15))
    show_button = Button(main_frame, text="Show Kanji", command=show_kanji_w)
    Button(main_frame, text="main menu", font=("Arial", 15), command=main_menu).grid(row=0, column=3)

    new_button.grid(row=0, column=0)
    prompt.grid(row=1, column=0, columnspan=2)
    feedback.grid(row=2, column=0, columnspan=2)
    show_button.grid(row=0, column=1)


def get_kanji_w():
    # this function gets a kanji from the session list and stores it in current char
    global current
    global main_frame
    global new_button
    global prompt
    global feedback
    global show_button
    global enter

    current = (current + 1) % len(session_list)
    prompt_text = "Draw the kanji character for " + session_list[current].english + " / " \
                  + session_list[current].japanese + ":"
    prompt.destroy()
    prompt = Label(main_frame, text=prompt_text, font=("Arial", 15))
    prompt.grid(row=1, column=0, columnspan=2)
    # The old prompt is erased and the prompt for the new kanji is created and displayed
    new_button["state"] = DISABLED
    show_button["state"] = NORMAL
    feedback.destroy()
    # The user is blocked from choosing a new kanji and the old feedback is removed to keep things running smooth


def show_kanji_w():
    # This function displays the current kanji
    global main_frame
    global current
    global feedback
    global show_button

    feedback.destroy()
    feedback = Label(main_frame, text=session_list[current].kanji, font=("IPAMincho", 80))
    feedback.grid(row=2, column=0, columnspan=2)
    show_button["state"] = DISABLED
    new_button["state"] = NORMAL


def counters_menu():
    # This function creates the menu that allows user to customize their counter study session
    global session_type
    global session_type_alt
    global main_frame

    for widget in main_frame.winfo_children():
        widget.destroy()

    session_type = StringVar()
    session_type.set("flashcard")
    session_type_alt = StringVar()
    session_type_alt.set("hiragana")

    type_label = Label(main_frame, text="Select the character type to study:", padx=50)
    session_label = Label(main_frame, text="Select which session type you would like:", padx=50)

    hir_button = Radiobutton(main_frame, text="hiragana", variable=session_type_alt, value="hiragana")
    kanji_button = Radiobutton(main_frame, text="kanji", variable=session_type_alt, value="kanji")

    flashcard = Radiobutton(main_frame, text="flashcards", variable=session_type, value="flashcard")
    test_session = Radiobutton(main_frame, text="test", variable=session_type, value="test")

    type_label.grid(row=0, column=0)
    hir_button.grid(row=1, column=0)
    kanji_button.grid(row=2, column=0)

    session_label.grid(row=0, column=1)
    flashcard.grid(row=1, column=1)
    test_session.grid(row=2, column=1)

    session_button = Button(main_frame, text="Create Session", command=create_counter_session, pady=10)

    session_button.grid(row=3, column=0, columnspan=1)


def create_counter_session():
    # This function creates a session by creating a session list and calling the counter session window function
    global main_frame
    global is_kanji
    global hiragana

    session_list.clear()

    for i in counter_list:
        session_list.append(i)

    counter_session_window()


def counter_session_window():
    # this function runs the number practice window
    global prompt
    global feedback
    global main_frame
    global new_button
    global answer
    global show_button
    global input_box
    global enter

    for widget in main_frame.winfo_children():
        widget.destroy()

    new_button = Button(main_frame, text="New prompt", command=get_counter)
    input_box = Entry(main_frame, font=("Arial", 30), width=35)
    enter = Button(main_frame, text="Enter", command=test_counter)
    if session_type.get() == "flashcard":
        enter["state"] = DISABLED
    prompt = Label(main_frame, text="Select the new prompt button to start practicing", font=("Arial", 15))
    feedback = Label(main_frame, text="Press the enter button to test your answer", font=("Arial", 15))
    show_button = Button(main_frame, text="Show Answer", command=show_counter)
    answer = Label(main_frame, text="", font=("Arial", 15))
    Button(main_frame, text="main menu", font=("Arial", 15), command=main_menu).grid(row=0, column=3)

    new_button.grid(row=1, column=0)
    input_box.grid(row=0, column=0, columnspan=3)
    enter.grid(row=1, column=2)
    prompt.grid(row=2, column=0, columnspan=3)
    feedback.grid(row=3, column=0, columnspan=3)
    show_button.grid(row=1, column=1)


def show_counter():
    # This function displays the current counter
    global main_frame
    global current_num
    global current
    global answer
    global show_button

    if answer.winfo_exists() == 1:
        answer.destroy()
    answer = Label(main_frame, text=counter_convert(str(current_num), current), font=("Arial", 15))
    answer.grid(row=4, column=0, columnspan=3)
    show_button["state"] = DISABLED
    if session_type.get() == "flashcard":
        new_button["state"] = NORMAL


def test_counter():
    # This function tests whether the entry is correct for the counter trainer
    global main_frame
    global input_box
    global new_button
    global feedback
    global current_num

    current_entry = input_box.get()
    if current_entry == counter_convert(current_num, current):
        if feedback.winfo_exists() == 1:
            feedback.destroy()
        feedback = Label(main_frame, text="correct", font=("Arial", 15))
        feedback.grid(row=3, column=0, columnspan=3)
        input_box.delete(0, "end")
        new_button["state"] = NORMAL
    else:
        if feedback.winfo_exists() == 1:
            feedback.destroy()
        feedback = Label(main_frame, text="incorrect", font=("Arial", 15))
        feedback.grid(row=3, column=0, columnspan=3)


def get_counter():
    # this function creates the number for the counter trainer
    global current_num
    global main_frame
    global new_button
    global prompt
    global feedback
    global current

    current = random.randint(0, len(session_list) - 1)
    if session_list[current].num_type == "12":
        current_num = random.randint(1, 12)
        if current_num <= 10:
            current_num = str(current_num)
        else:
            current_num = "how many"
    else:
        current_num = random.randint(1, 120)
        if current_num <= 99:
            current_num = str(current_num)
        else:
            current_num = "how many"
    prompt_text = ""
    if session_type_alt.get() == "hiragana":
        prompt_text = "Enter the Hiragana for " + str(current_num) + " " + session_list[current].english + ":"
    if session_type_alt.get() == "kanji":
        prompt_text = "Enter the Hiragana for " + counter_kanji(current_num, current) + ":"
    prompt.destroy()
    prompt = Label(main_frame, text=prompt_text, font=("Arial", 15))
    prompt.grid(row=2, column=0, columnspan=3)
    new_button["state"] = DISABLED
    show_button["state"] = NORMAL
    feedback.destroy()
    if session_type.get() == "flashcard":
        answer.destroy()


def counter_convert(curr_num, curr):
    converted = ""

    num_dict = {"1": "いち",
                "2": "に",
                "3": "さん",
                "4": "よん",
                "5": "ご",
                "6": "ろく",
                "7": "なな",
                "8": "はち",
                "9": "きゅう",
                "10": "じゅう",
                "how many": "なん"}

    # The number is converted to as much hiragana as possible and the critical number is determined
    if curr_num == "how many":
        crit_value = "how many"
    else:
        if len(curr_num) == 1:
            crit_value = curr_num
        else:
            if curr_num[0] != "1":
                converted += num_dict[curr_num[0]]
            if curr_num[1] != "0":
                converted += "じゅう"
                crit_value = curr_num[1]
            else:
                crit_value = "10"

    if session_list[curr].num_type == "1":
        converted += num_dict[crit_value]
        converted += session_list[curr].japanese

    if session_list[curr].num_type == "2":
        if crit_value == "4":
            converted += "よ"

        elif crit_value == "7":
            converted += "しち"

        elif crit_value == "9":
            converted += "く"

        else:
            converted += num_dict[crit_value]

        converted += session_list[curr].japanese

    if session_list[curr].num_type == "3":
        if crit_value == "4":
            converted += "よ"
        else:
            converted += num_dict[crit_value]

        converted += session_list[curr].japanese

    if session_list[curr].num_type == "4":
        item = session_list[curr].japanese

        if crit_value == "1":
            converted += "いっ"
            if item[0] == "ふ":
                item = item.replace("ふ", "ぷ", 1)

        elif crit_value == "3":
            converted += num_dict[crit_value]
            if item[0] == "ふ":
                item = item.replace("ふ", "ぷ", 1)

        elif crit_value == "4":
            converted += num_dict[crit_value]
            if item[0] == "ふ":
                item = item.replace("ふ", "ぷ", 1)

        elif crit_value == "6":
            converted += "ろっ"
            if item[0] == "ふ":
                item = item.replace("ふ", "ぷ", 1)

        elif crit_value == "8":
            converted += "はっ"
            if item[0] == "ふ":
                item = item.replace("ふ", "ぷ", 1)

        elif crit_value == "10":
            converted += "じゅっ"
            if item[0] == "ふ":
                item = item.replace("ふ", "ぷ", 1)

        elif crit_value == "how many":
            converted += num_dict[crit_value]
            if item[0] == "ふ":
                item = item.replace("ふ", "ぷ", 1)

        else:
            converted += num_dict[crit_value]

        converted += item

    if session_list[curr].num_type == "5":
        item = session_list[curr].japanese

        if crit_value == "1":
            converted += "いっ"
            if item[0] == "は":
                item = item.replace("は", "ぱ", 1)
            if item[0] == "ほ":
                item = item.replace("ほ", "ぽ", 1)
            if item[0] == "ひ":
                item = item.replace("ひ", "ぴ", 1)

        elif crit_value == "3":
            converted += num_dict[crit_value]
            if item[0] == "は":
                item = item.replace("は", "ば", 1)
            if item[0] == "ほ":
                item = item.replace("ほ", "ぼ", 1)
            if item[0] == "ひ":
                item = item.replace("ひ", "び", 1)

        elif crit_value == "6":
            converted += "ろっ"
            if item[0] == "は":
                item = item.replace("は", "ぱ", 1)
            if item[0] == "ほ":
                item = item.replace("ほ", "ぽ", 1)
            if item[0] == "ひ":
                item = item.replace("ひ", "ぴ", 1)

        elif crit_value == "8":
            converted += "はっ"
            if item[0] == "は":
                item = item.replace("は", "ぱ", 1)
            if item[0] == "ほ":
                item = item.replace("ほ", "ぽ", 1)
            if item[0] == "ひ":
                item = item.replace("ひ", "ぴ", 1)

        elif crit_value == "10":
            if item[0] == "は":
                item = item.replace("は", "ぱ", 1)
            if item[0] == "ほ":
                item = item.replace("ほ", "ぽ", 1)
            if item[0] == "ひ":
                item = item.replace("ひ", "ぴ", 1)

        elif crit_value == "how many":
            converted += num_dict[crit_value]
            if item[0] == "は":
                item = item.replace("は", "ば", 1)
            if item[0] == "ほ":
                item = item.replace("ほ", "ぼ", 1)
            if item[0] == "ひ":
                item = item.replace("ひ", "び", 1)

        else:
            converted += num_dict[crit_value]

        converted += item

    if session_list[curr].num_type == "6" or session_list[curr].num_type == "7":
        if crit_value == "1":
            converted += "いっ"

        elif crit_value == "6":
            converted += "ろっ"

        elif crit_value == "8":
            converted += "はっ"

        elif crit_value == "10":
            converted += "じゅっ"

        else:
            converted += num_dict[crit_value]

        converted += session_list[curr].japanese

    if session_list[curr].num_type == "8":
        item = session_list[curr].japanese

        if crit_value == "1":
            converted += "いっ"

        elif crit_value == "3":
            converted += num_dict[crit_value]
            if item[0] == "か":
                item = item.replace("か", "が", 1)
            if item[0] == "け":
                item = item.replace("け", "げ", 1)

        elif crit_value == "6":
            converted += "ろっ"

        elif crit_value == "8":
            converted += "はっ"

        elif crit_value == "10":
            converted += "じゅっ"

        elif crit_value == "how many":
            converted += num_dict[crit_value]
            if item[0] == "か":
                item = item.replace("か", "が", 1)
            if item[0] == "け":
                item = item.replace("け", "げ", 1)

        else:
            converted += num_dict[crit_value]

        converted += item

    if session_list[curr].num_type == "9" or session_list[curr].num_type == "11":
        if crit_value == "1":
            converted += "いっ"
        elif crit_value == "8":
            converted += "はっ"
        elif crit_value == "10":
            converted += "じゅっ"

        else:
            converted += num_dict[crit_value]

        converted += session_list[curr].japanese

    if session_list[curr].num_type == "10":
        item = session_list[curr].japanese

        if crit_value == "1":
            converted += "いっ"

        elif crit_value == "3":
            converted += num_dict[crit_value]
            if item[0] == "そ":
                item = item.replace("そ", "ぞ", 1)
            if item[0] == "せ":
                item = item.replace("せ", "ぜ", 1)

        elif crit_value == "8":
            converted += "はっ"

        elif crit_value == "10":
            converted += "じゅっ"

        elif crit_value == "how many":
            converted += num_dict[crit_value]
            if item[0] == "そ":
                item = item.replace("そ", "ぞ", 1)
            if item[0] == "せ":
                item = item.replace("せ", "ぜ", 1)

        else:
            converted += num_dict[crit_value]

        converted += item

    if session_list[curr].num_type == "12":
        if crit_value == "1":
            converted += "ひとつ"

        if crit_value == "2":
            converted += "ふたつ"

        if crit_value == "3":
            converted += "みっつ"

        if crit_value == "4":
            converted += "よっつ"

        if crit_value == "5":
            converted += "いつつ"

        if crit_value == "6":
            converted += "むっつ"

        if crit_value == "7":
            converted += "ななつ"

        if crit_value == "8":
            converted += "やっつ"

        if crit_value == "9":
            converted += "ここのつ"

        if crit_value == "10":
            converted += "とお"

        if crit_value == "how many":
            converted += "いくつ"

    if session_list[curr].num_type == "13":
        item = session_list[curr].japanese

        if crit_value == "1":
            converted += "ひとり"
            item = ""

        elif crit_value == "2":
            converted += "ふたり"
            item = ""

        elif crit_value == "4":
            converted += "よ"

        else:
            converted += num_dict[crit_value]

        converted += item

    return converted


def counter_kanji(curr_num, curr):
    converted = ""

    if curr_num != "how many":
        converted += num_kanji(curr_num)
    else:
        if session_list[curr].japanese != "つ":
            converted += "何"
        else:
            converted += "幾"

    if session_list[curr].kanji == "":
        converted += session_list[curr].japanese
    else:
        converted += session_list[curr].kanji

    return converted


def shuffle_list(a_list):
    # This function randomizes a list using swaps
    for i in range(len(a_list)):
        j = random.randint(0, len(a_list) - 1)
        temp = a_list[j]
        a_list[j] = a_list[i]
        a_list[i] = temp


def study_menu():
    # This is the main loop that the program runs in

    global main_frame

    for widget in main_frame.winfo_children():
        widget.destroy()

    Label(main_frame, text="select what you would like to study below").pack()

    Button(main_frame, text="Characters", command=character_menu).pack()
    Button(main_frame, text="Character Writing", command=character_w_menu).pack()
    Button(main_frame, text="Vocabulary", command=vocab_menu).pack()
    Button(main_frame, text="Particles", command=particle_menu).pack()
    Button(main_frame, text="Numbers", command=num_menu).pack()
    Button(main_frame, text="Time", command=time_menu).pack()
    Button(main_frame, text="Calendar", command=calendar_menu).pack()
    Button(main_frame, text="Verb Conjugation", command=verb_menu).pack()
    Button(main_frame, text="Adjective Conjugation", command=adjective_menu).pack()
    Button(main_frame, text="Kanji Identification", command=kanji_menu).pack()
    Button(main_frame, text="Kanji Writing", command=kanji_w_menu).pack()
    Button(main_frame, text="Counters", command=counters_menu).pack()


def settings():
    global window_width
    global window_height
    global window_option
    global root
    global main_frame

    for widget in main_frame.winfo_children():
        widget.destroy()

    Label(main_frame, text="setting menu").grid(row=0, column=0)
    Label(main_frame, text="window size").grid(row=1, column=0)

    full_screen_button = Radiobutton(main_frame, text="fullscreen", variable=window_option, value="fullscreen")
    detected_button = Radiobutton(main_frame, text="detected screen size", variable=window_option,
                                  value="detected screen size")
    custom_button = Radiobutton(main_frame, text="custom", variable=window_option, value="custom")
    Button(main_frame, text="main menu", font=("Arial", 15), command=main_menu).grid(row=0, column=3)

    full_screen_button.grid(row=2, column=0)
    detected_button.grid(row=3, column=0)
    custom_button.grid(row=4, column=0)

    width_option = Entry(main_frame, font=("Arial", 15), width=10)
    height_option = Entry(main_frame, font=("Arial", 15), width=10)

    width_option.grid(row=5, column=0)
    height_option.grid(row=6, column=0)

    apply_button = Button(main_frame, text="apply", command=lambda: apply(width_option.get(), height_option.get()))

    apply_button.grid(row=7, column=0)


def apply(width, height):
    global window_width
    global window_height
    global window_option
    global root
    global main_frame

    for widget in main_frame.winfo_children():
        widget.destroy()
    main_frame.destroy()

    if window_option.get() == "fullscreen":
        root.attributes('-fullscreen', True)
        window_width = root.winfo_screenwidth()
        window_height = root.winfo_screenheight()
        width_offset = (int(root.winfo_screenwidth() / 2)) - (int(window_width / 2))
        height_offset = (int(root.winfo_screenheight() / 2)) - (int(window_height / 2))
        root.geometry(str(window_width) + "x" + str(window_height) + "+" + str(width_offset) + "+" + str(height_offset))

    elif window_option.get() == "detected screen size":
        root.attributes('-fullscreen', False)
        window_width = root.winfo_screenwidth()
        window_height = root.winfo_screenheight()
        width_offset = (int(root.winfo_screenwidth() / 2)) - (int(window_width / 2))
        height_offset = (int(root.winfo_screenheight() / 2)) - (int(window_height / 2))
        root.geometry(str(window_width) + "x" + str(window_height) + "+" + str(width_offset) + "+" + str(height_offset))

    elif window_option.get() == "custom":
        root.attributes('-fullscreen', False)
        window_width = int(width)
        window_height = int(height)
        width_offset = (int(root.winfo_screenwidth() / 2)) - (int(window_width / 2))
        height_offset = (int(root.winfo_screenheight() / 2)) - (int(window_height / 2))
        root.geometry(str(window_width) + "x" + str(window_height) + "+" + str(width_offset) + "+" + str(height_offset))

    main_frame = LabelFrame(root, borderwidth=0, highlightthickness=0)
    main_frame.pack()

    settings()


def main_menu():
    # This is the main loop that the program runs in
    global main_frame

    for widget in main_frame.winfo_children():
        widget.destroy()

    Label(main_frame, text="welcome to the japanese trainer").grid(row=0, column=0)

    Button(main_frame, text="Study", command=study_menu).grid(row=1, column=0)
    Button(main_frame, text="Settings", command=settings).grid(row=2, column=0)


def launch():
    global window_width
    global window_height
    global main_frame
    global window_option
    global root

    window_width = root.winfo_screenwidth()
    window_height = root.winfo_screenheight()
    width_offset = (int(root.winfo_screenwidth() / 2)) - (int(window_width / 2))
    height_offset = (int(root.winfo_screenheight() / 2)) - (int(window_height / 2))
    window_option = StringVar()
    window_option.set("fullscreen")
    root.geometry(str(window_width) + "x" + str(window_height) + "+" + str(width_offset) + "+" + str(height_offset))
    if window_option.get() == "fullscreen":
        root.attributes('-fullscreen', True)
    root.title("Japanese Trainer")
    main_frame = LabelFrame(root, borderwidth=0, highlightthickness=0)
    main_frame.pack()

    main_menu()


if __name__ == "__main__":
    root = Tk()
    launch()
    root.mainloop()
