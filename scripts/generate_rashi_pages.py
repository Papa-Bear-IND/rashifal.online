#!/usr/bin/env python3
"""Generate 12 individual rashi HTML pages with unique content for SEO + AdSense eligibility."""

import json, os

RASHIS = [
    {
        "id": "mesh", "file": "mesh.html",
        "hi": "मेष", "en": "Aries", "sym": "Ar",
        "dates_hi": "21 मार्च – 19 अप्रैल", "dates_en": "March 21 – April 19",
        "element_hi": "अग्नि", "element_en": "Fire",
        "ruler_hi": "मंगल", "ruler_en": "Mars",
        "quality_hi": "चर (Cardinal)", "quality_en": "Cardinal",
        "lucky_day_hi": "मंगलवार", "lucky_day_en": "Tuesday",
        "lucky_gem_hi": "मूंगा (Red Coral)", "lucky_gem_en": "Red Coral (Moonga)",
        "lucky_color_hi": "लाल", "lucky_color_en": "Red",
        "lucky_num": "9",
        "body_hi": "सिर और मस्तिष्क", "body_en": "Head and brain",
        "compatible_hi": "सिंह, धनु, मिथुन", "compatible_en": "Leo, Sagittarius, Gemini",
        "incompatible_hi": "कर्क, मकर", "incompatible_en": "Cancer, Capricorn",
        "famous": "अजय देवगन, लेडी गागा, रॉबर्ट डाउनी जूनियर, कंगना रनौत",
        "personality_hi": """मेष राशि के जातक स्वभाव से साहसी, ऊर्जावान और नेतृत्व करने वाले होते हैं। मंगल ग्रह इनके स्वामी हैं, जिसके कारण इनमें अदम्य साहस और जोश भरा रहता है। ये किसी भी कार्य को शुरू करने में सबसे आगे रहते हैं और चुनौतियों से कभी नहीं घबराते।

इनका व्यक्तित्व प्रभावशाली होता है और ये अपने विचारों को स्पष्ट रूप से व्यक्त करते हैं। हालांकि कभी-कभी इनका स्वभाव आवेगपूर्ण हो सकता है और ये जल्दबाजी में निर्णय ले लेते हैं। धैर्य रखना इनके लिए सबसे बड़ी सीख है।

करियर में ये प्रशासन, सेना, पुलिस, खेल और उद्यमिता जैसे क्षेत्रों में उत्कृष्ट प्रदर्शन करते हैं। इनके लिए ऐसा कार्य उपयुक्त है जहाँ नेतृत्व की भूमिका हो और स्वतंत्रता से काम करने का अवसर मिले।

स्वास्थ्य के मामले में इन्हें सिरदर्द, रक्तचाप और अत्यधिक थकान की समस्या हो सकती है। नियमित व्यायाम और संतुलित आहार इनके स्वास्थ्य की कुंजी है। मानसिक शांति के लिए ध्यान और योग अत्यंत लाभकारी है।""",
        "personality_en": """Aries individuals are born leaders — courageous, energetic, and always ready to take charge. Ruled by Mars, they possess an indomitable spirit and an infectious enthusiasm that inspires everyone around them. They are the pioneers of the zodiac, always eager to start new ventures and blaze new trails.

Their personality is magnetic and direct. Aries natives say what they mean and mean what they say. However, this directness can sometimes come across as impatience or impulsiveness. Learning to pause before reacting is their greatest life lesson.

In career, Aries thrives in roles that demand leadership, courage, and quick decision-making — military, sports, entrepreneurship, emergency services, and executive positions. They perform best when given autonomy and a clear mission.

Health-wise, Aries should watch for headaches, high blood pressure, and burnout from overexertion. Regular exercise is essential but so is rest. Meditation and yoga can help channel their abundant Mars energy constructively rather than destructively.""",
        "strengths_hi": "साहसी, ऊर्जावान, आत्मविश्वासी, नेतृत्वकर्ता, निर्णायक",
        "strengths_en": "Courageous, energetic, confident, natural leader, decisive",
        "weaknesses_hi": "आवेगी, अधीर, अहंकारी, जिद्दी, आक्रामक",
        "weaknesses_en": "Impulsive, impatient, egoistic, stubborn, aggressive",
        "love_hi": "मेष राशि के लोग प्रेम में बहुत भावुक और समर्पित होते हैं। ये अपने साथी के लिए कुछ भी करने को तैयार रहते हैं। हालांकि इनका अधिकार भाव कभी-कभी रिश्ते में तनाव पैदा कर सकता है। सिंह और धनु राशि के साथ इनकी सबसे अच्छी जोड़ी बनती है।",
        "love_en": "In love, Aries is passionate, devoted, and fiercely loyal. They pursue their romantic interests with the same intensity they bring to everything else. Their ideal partners are those who can match their energy while also grounding them. Best matches are Leo and Sagittarius — fellow fire signs who understand their need for excitement.",
    },
    {
        "id": "vrishabh", "file": "vrishabh.html",
        "hi": "वृषभ", "en": "Taurus", "sym": "Ta",
        "dates_hi": "20 अप्रैल – 20 मई", "dates_en": "April 20 – May 20",
        "element_hi": "पृथ्वी", "element_en": "Earth",
        "ruler_hi": "शुक्र", "ruler_en": "Venus",
        "quality_hi": "स्थिर (Fixed)", "quality_en": "Fixed",
        "lucky_day_hi": "शुक्रवार", "lucky_day_en": "Friday",
        "lucky_gem_hi": "हीरा (Diamond)", "lucky_gem_en": "Diamond (Heera)",
        "lucky_color_hi": "सफ़ेद, हरा", "lucky_color_en": "White, Green",
        "lucky_num": "6",
        "body_hi": "गला और कंठ", "body_en": "Throat and neck",
        "compatible_hi": "कन्या, मकर, कर्क", "compatible_en": "Virgo, Capricorn, Cancer",
        "incompatible_hi": "सिंह, कुम्भ", "incompatible_en": "Leo, Aquarius",
        "famous": "सचिन तेंदुलकर, डेविड बेकहम, अनुष्का शर्मा, मार्क ज़करबर्ग",
        "personality_hi": """वृषभ राशि के जातक स्थिर, विश्वसनीय और व्यावहारिक स्वभाव के होते हैं। शुक्र ग्रह के स्वामित्व में ये सौंदर्य, कला और भौतिक सुखों के प्रेमी होते हैं। इनका जीवन के प्रति दृष्टिकोण ठोस और यथार्थवादी होता है।

ये लोग धैर्यवान होते हैं और किसी भी कार्य को पूरा करने में कोई कसर नहीं छोड़ते। एक बार जो ठान लें उसे पूरा करके ही रहते हैं। हालांकि इनकी जिद कभी-कभी समस्या बन सकती है और बदलाव को स्वीकार करने में कठिनाई होती है।

करियर में ये बैंकिंग, वित्त, रियल एस्टेट, कला, संगीत और खाद्य उद्योग में सफल होते हैं। आर्थिक सुरक्षा इनके लिए सर्वोच्च प्राथमिकता है और ये धन संचय में कुशल होते हैं।

स्वास्थ्य के संदर्भ में गले, थायरॉइड और वज़न बढ़ने की समस्या हो सकती है। संतुलित भोजन और नियमित सैर इनके स्वास्थ्य के लिए आवश्यक है।""",
        "personality_en": """Taurus individuals are the rock of the zodiac — stable, dependable, and deeply practical. Ruled by Venus, they have an innate appreciation for beauty, comfort, and the finer things in life. They approach everything with a grounded, no-nonsense attitude that others find reassuring.

Patience is their superpower. Where other signs rush and stumble, Taurus moves steadily toward their goals with unwavering determination. However, this same quality can manifest as stubbornness — once they've made up their mind, changing it requires an act of divine intervention.

Career-wise, Taurus excels in finance, banking, real estate, agriculture, music, culinary arts, and luxury goods. They are natural wealth builders who understand the value of long-term investment and steady accumulation.

Health considerations include thyroid issues, throat problems, and weight management. Taurus loves comfort food, which can lead to overindulgence. Regular walks in nature and a disciplined eating schedule work wonders for their constitution.""",
        "strengths_hi": "धैर्यवान, विश्वसनीय, व्यावहारिक, समर्पित, कलाप्रेमी",
        "strengths_en": "Patient, reliable, practical, devoted, artistic",
        "weaknesses_hi": "जिद्दी, आलसी, अधिकार-भाव, भौतिकवादी, परिवर्तन से भय",
        "weaknesses_en": "Stubborn, lazy, possessive, materialistic, resistant to change",
        "love_hi": "वृषभ राशि प्रेम में अत्यंत समर्पित और वफ़ादार होती है। ये अपने साथी को सुरक्षा और स्थिरता प्रदान करते हैं। शारीरिक स्पर्श इनकी प्रेम भाषा है। कन्या और मकर राशि के साथ सबसे गहरा जुड़ाव होता है।",
        "love_en": "In love, Taurus is deeply loyal, sensual, and devoted. They express love through physical affection, home-cooked meals, and creating a beautiful shared space. They seek partners who value stability and loyalty as much as they do. Best matches are Virgo and Capricorn — fellow earth signs who share their practical approach to love.",
    },
    {
        "id": "mithun", "file": "mithun.html",
        "hi": "मिथुन", "en": "Gemini", "sym": "Ge",
        "dates_hi": "21 मई – 20 जून", "dates_en": "May 21 – June 20",
        "element_hi": "वायु", "element_en": "Air",
        "ruler_hi": "बुध", "ruler_en": "Mercury",
        "quality_hi": "द्विस्वभाव (Mutable)", "quality_en": "Mutable",
        "lucky_day_hi": "बुधवार", "lucky_day_en": "Wednesday",
        "lucky_gem_hi": "पन्ना (Emerald)", "lucky_gem_en": "Emerald (Panna)",
        "lucky_color_hi": "हरा, पीला", "lucky_color_en": "Green, Yellow",
        "lucky_num": "5",
        "body_hi": "फेफड़े, हाथ और कंधे", "body_en": "Lungs, arms, and shoulders",
        "compatible_hi": "तुला, कुम्भ, मेष", "compatible_en": "Libra, Aquarius, Aries",
        "incompatible_hi": "कन्या, मीन", "incompatible_en": "Virgo, Pisces",
        "famous": "अमिताभ बच्चन, जॉनी डेप, एंजेलीना जोली, सोनम कपूर",
        "personality_hi": """मिथुन राशि के जातक बुद्धिमान, चतुर और संवाद कुशल होते हैं। बुध ग्रह के प्रभाव से इनकी वाक्पटुता और तर्कशक्ति अद्वितीय होती है। ये हर विषय में रुचि रखते हैं और नई-नई जानकारी प्राप्त करने के लिए सदैव उत्सुक रहते हैं।

इनका व्यक्तित्व बहुमुखी होता है — ये एक साथ कई कार्यों को संभाल सकते हैं। हालांकि इसी कारण कभी-कभी किसी एक कार्य पर ध्यान केंद्रित करना कठिन हो जाता है। चंचल स्वभाव इनकी पहचान है।

करियर में ये पत्रकारिता, लेखन, शिक्षा, विपणन, जनसंपर्क और सूचना प्रौद्योगिकी में उत्कृष्ट प्रदर्शन करते हैं। जहाँ भी संवाद और विचारों का आदान-प्रदान हो, वहाँ मिथुन राशि के लोग चमकते हैं।

स्वास्थ्य में श्वसन तंत्र, कंधे और तंत्रिका तंत्र से संबंधित समस्याएं हो सकती हैं। मानसिक अशांति और नींद की कमी भी एक चुनौती हो सकती है।""",
        "personality_en": """Gemini is the communicator of the zodiac — witty, intellectual, and endlessly curious. Ruled by Mercury, they possess a quicksilver mind that can process information faster than most signs. They are natural storytellers, teachers, and networkers who thrive on mental stimulation.

Their dual nature means they can see every situation from multiple perspectives, making them excellent mediators and problem-solvers. However, this same duality can make them seem inconsistent or unreliable to those who don't understand them.

Career paths that suit Gemini include journalism, writing, teaching, marketing, public relations, IT, and social media. Any field that rewards communication skills and adaptability is their playground.

Health-wise, Gemini should pay attention to respiratory health, nervous system, and sleep quality. Their restless mind can lead to anxiety and insomnia if not managed through mindfulness practices and regular digital detox.""",
        "strengths_hi": "बुद्धिमान, संवाद कुशल, बहुमुखी, अनुकूलनशील, जिज्ञासु",
        "strengths_en": "Intelligent, communicative, versatile, adaptable, curious",
        "weaknesses_hi": "चंचल, असंगत, सतही, अनिर्णायक, अस्थिर",
        "weaknesses_en": "Restless, inconsistent, superficial, indecisive, nervous",
        "love_hi": "मिथुन राशि प्रेम में बौद्धिक जुड़ाव चाहती है। इनके लिए अच्छी बातचीत किसी भी उपहार से बड़ी है। ये चुलबुले और रोमांटिक होते हैं लेकिन एकरसता से ऊब जाते हैं। तुला और कुम्भ राशि के साथ इनकी बेहतरीन केमिस्ट्री होती है।",
        "love_en": "Gemini seeks intellectual connection in love above all else. A great conversation is their idea of the perfect date. They are playful, flirtatious, and need variety to stay engaged. Best matches are Libra and Aquarius — fellow air signs who can keep up with their mental pace.",
    },
    {
        "id": "kark", "file": "kark.html",
        "hi": "कर्क", "en": "Cancer", "sym": "Ca",
        "dates_hi": "21 जून – 22 जुलाई", "dates_en": "June 21 – July 22",
        "element_hi": "जल", "element_en": "Water",
        "ruler_hi": "चंद्रमा", "ruler_en": "Moon",
        "quality_hi": "चर (Cardinal)", "quality_en": "Cardinal",
        "lucky_day_hi": "सोमवार", "lucky_day_en": "Monday",
        "lucky_gem_hi": "मोती (Pearl)", "lucky_gem_en": "Pearl (Moti)",
        "lucky_color_hi": "सफ़ेद, चाँदी", "lucky_color_en": "White, Silver",
        "lucky_num": "2",
        "body_hi": "छाती और पेट", "body_en": "Chest and stomach",
        "compatible_hi": "वृश्चिक, मीन, वृषभ", "compatible_en": "Scorpio, Pisces, Taurus",
        "incompatible_hi": "मेष, तुला", "incompatible_en": "Aries, Libra",
        "famous": "प्रियंका चोपड़ा, सेलेना गोमेज़, एम.एस. धोनी, मर्सल प्रूस्त",
        "personality_hi": """कर्क राशि के जातक अत्यंत भावुक, संवेदनशील और परिवार-प्रेमी होते हैं। चंद्रमा इनके स्वामी ग्रह हैं, जिसके कारण इनका मन अत्यंत कोमल और सहज ज्ञान से भरपूर होता है। ये अपने प्रियजनों की रक्षा के लिए कुछ भी कर सकते हैं।

इनका घर इनका किला है — ये गृहस्थी में अत्यंत निपुण होते हैं और अपने घर को सजाना-संवारना पसंद करते हैं। भोजन बनाना, परिवार की देखभाल और एक आरामदायक वातावरण बनाना इनकी विशेषता है।

करियर में ये नर्सिंग, शिक्षा, होटल उद्योग, रियल एस्टेट, मनोविज्ञान और सामाजिक कार्य में उत्कृष्ट होते हैं। जहाँ भी देखभाल और सहानुभूति की आवश्यकता हो, कर्क राशि वहाँ चमकती है।

स्वास्थ्य में पेट की समस्याएं, अपच, जल प्रतिधारण और भावनात्मक खान-पान की प्रवृत्ति हो सकती है। मानसिक स्वास्थ्य पर विशेष ध्यान देना आवश्यक है।""",
        "personality_en": """Cancer is the nurturer of the zodiac — deeply emotional, intuitive, and fiercely protective of loved ones. Ruled by the Moon, their moods ebb and flow like lunar tides, giving them an almost psychic ability to sense others' emotions before a word is spoken.

Home is their sanctuary. Cancer individuals create warm, inviting spaces where family and friends feel safe and loved. They are natural homemakers, excellent cooks, and the emotional backbone of any family or group.

Career paths that align with Cancer include nursing, teaching, hospitality, real estate, psychology, social work, and the food industry. They excel in any role that requires empathy, emotional intelligence, and caregiving.

Health considerations include digestive issues, water retention, emotional eating, and anxiety. Cancer must guard against absorbing others' negative emotions. Setting emotional boundaries and practicing self-care is essential for their wellbeing.""",
        "strengths_hi": "भावुक, सहज ज्ञानी, देखभाल करने वाला, वफ़ादार, कल्पनाशील",
        "strengths_en": "Emotional, intuitive, caring, loyal, imaginative",
        "weaknesses_hi": "मूडी, असुरक्षित, अतिसंवेदनशील, अधिकार-भाव, बीते कल में जीना",
        "weaknesses_en": "Moody, insecure, oversensitive, possessive, dwelling on the past",
        "love_hi": "कर्क राशि प्रेम में पूर्ण समर्पण चाहती है। ये गहरे भावनात्मक जुड़ाव के बिना संतुष्ट नहीं होते। इनके लिए प्रेम का अर्थ सुरक्षा, देखभाल और घर जैसा आराम है। वृश्चिक और मीन राशि से सबसे गहरा जुड़ाव होता है।",
        "love_en": "Cancer loves deeply and completely. They seek emotional security above all else in a relationship. For them, love means building a home together, sharing meals, and creating lasting memories. Best matches are Scorpio and Pisces — fellow water signs who understand the depth of their emotions.",
    },
    {
        "id": "singh", "file": "singh.html",
        "hi": "सिंह", "en": "Leo", "sym": "Le",
        "dates_hi": "23 जुलाई – 22 अगस्त", "dates_en": "July 23 – August 22",
        "element_hi": "अग्नि", "element_en": "Fire",
        "ruler_hi": "सूर्य", "ruler_en": "Sun",
        "quality_hi": "स्थिर (Fixed)", "quality_en": "Fixed",
        "lucky_day_hi": "रविवार", "lucky_day_en": "Sunday",
        "lucky_gem_hi": "माणिक (Ruby)", "lucky_gem_en": "Ruby (Manik)",
        "lucky_color_hi": "सुनहरा, नारंगी", "lucky_color_en": "Gold, Orange",
        "lucky_num": "1",
        "body_hi": "हृदय और रीढ़", "body_en": "Heart and spine",
        "compatible_hi": "मेष, धनु, मिथुन", "compatible_en": "Aries, Sagittarius, Gemini",
        "incompatible_hi": "वृषभ, वृश्चिक", "incompatible_en": "Taurus, Scorpio",
        "famous": "शाहरुख़ ख़ान, बराक ओबामा, मैडोना, सैफ़ अली ख़ान",
        "personality_hi": """सिंह राशि के जातक जन्मजात नेता होते हैं — आत्मविश्वासी, उदार और प्रभावशाली। सूर्य इनके स्वामी ग्रह हैं, जिसके कारण जहाँ भी ये जाते हैं, अपनी उपस्थिति से प्रकाश फैलाते हैं। ये किसी भी समूह का केंद्र बिंदु होते हैं।

इनमें रचनात्मकता और कलात्मकता कूट-कूट कर भरी होती है। ये मंच पर हों या कार्यालय में — हर जगह अपनी छाप छोड़ते हैं। प्रशंसा और सम्मान इनके लिए प्राण वायु के समान है।

करियर में ये अभिनय, राजनीति, प्रबंधन, शिक्षा, फ़ैशन और मनोरंजन उद्योग में शानदार प्रदर्शन करते हैं। नेतृत्व की भूमिका इनके लिए स्वाभाविक है।

स्वास्थ्य में हृदय, रीढ़ और रक्तचाप से संबंधित समस्याएं हो सकती हैं। इन्हें तनाव प्रबंधन और नियमित हृदय व्यायाम पर ध्यान देना चाहिए।""",
        "personality_en": """Leo is the king of the zodiac — confident, generous, and born to lead. Ruled by the Sun, they radiate warmth and charisma wherever they go. They are the natural center of attention in any room, not because they demand it, but because their energy is simply magnetic.

Creativity runs deep in Leo. Whether on stage, in the boardroom, or at a dinner party, they have a flair for the dramatic and an ability to inspire others. Recognition and appreciation fuel their fire — without it, even the brightest Leo can dim.

Career paths ideal for Leo include acting, politics, management, education, fashion, entertainment, and luxury brands. They are born for roles where they can lead, inspire, and be visible.

Health-wise, Leo should focus on heart health, spine care, and blood pressure management. Their tendency to take on too much responsibility can lead to stress-related issues. Regular cardiovascular exercise and creative outlets are essential.""",
        "strengths_hi": "आत्मविश्वासी, उदार, रचनात्मक, वफ़ादार, प्रेरणादायक",
        "strengths_en": "Confident, generous, creative, loyal, inspiring",
        "weaknesses_hi": "अहंकारी, अधिकार-भाव, हठी, दिखावा-पसंद, आलोचना से आहत",
        "weaknesses_en": "Arrogant, dominating, stubborn, vain, sensitive to criticism",
        "love_hi": "सिंह राशि प्रेम में भव्य और रोमांटिक होती है। ये अपने साथी को राजा-रानी की तरह रखते हैं और बदले में वैसा ही सम्मान चाहते हैं। मेष और धनु राशि के साथ सबसे तीव्र रसायन होता है।",
        "love_en": "Leo loves grandly and dramatically. They shower their partner with attention, gifts, and affection, and expect the same royal treatment in return. Best matches are Aries and Sagittarius — fellow fire signs who appreciate their warmth and don't compete for the spotlight.",
    },
    {
        "id": "kanya", "file": "kanya.html",
        "hi": "कन्या", "en": "Virgo", "sym": "Vi",
        "dates_hi": "23 अगस्त – 22 सितम्बर", "dates_en": "August 23 – September 22",
        "element_hi": "पृथ्वी", "element_en": "Earth",
        "ruler_hi": "बुध", "ruler_en": "Mercury",
        "quality_hi": "द्विस्वभाव (Mutable)", "quality_en": "Mutable",
        "lucky_day_hi": "बुधवार", "lucky_day_en": "Wednesday",
        "lucky_gem_hi": "पन्ना (Emerald)", "lucky_gem_en": "Emerald (Panna)",
        "lucky_color_hi": "हरा, भूरा", "lucky_color_en": "Green, Brown",
        "lucky_num": "5",
        "body_hi": "पाचन तंत्र और आंतें", "body_en": "Digestive system and intestines",
        "compatible_hi": "वृषभ, मकर, कर्क", "compatible_en": "Taurus, Capricorn, Cancer",
        "incompatible_hi": "मिथुन, धनु", "incompatible_en": "Gemini, Sagittarius",
        "famous": "नरेंद्र मोदी, कीनू रीव्स, बेयॉन्से, अक्षय कुमार",
        "personality_hi": """कन्या राशि के जातक विश्लेषक, व्यवस्थित और पूर्णतावादी होते हैं। बुध ग्रह के प्रभाव से इनकी बुद्धि तीक्ष्ण और विवेकशील होती है। ये हर कार्य को सूक्ष्मता से देखते हैं और छोटी से छोटी बात पर ध्यान देते हैं।

सेवा भाव इनके स्वभाव में है — ये दूसरों की मदद करने में सच्चा आनंद पाते हैं। हालांकि अत्यधिक आलोचनात्मक स्वभाव कभी-कभी इन्हें और दूसरों को परेशान कर सकता है।

करियर में ये स्वास्थ्य सेवा, लेखांकन, अनुसंधान, संपादन, गुणवत्ता नियंत्रण और डेटा विश्लेषण में उत्कृष्ट होते हैं। जहाँ भी सटीकता और विश्लेषण की ज़रूरत है, कन्या राशि वहाँ अपना स्थान बनाती है।

स्वास्थ्य में पाचन समस्याएं, चिंता और अत्यधिक तनाव की प्रवृत्ति हो सकती है। स्वस्थ आहार और मानसिक शांति इनके लिए अत्यंत महत्वपूर्ण है।""",
        "personality_en": """Virgo is the perfectionist of the zodiac — analytical, organized, and deeply dedicated to service. Ruled by Mercury, they possess a sharp, discerning intellect that notices details others miss entirely. They are the ones who read the fine print and actually understand it.

Their desire to help is genuine and tireless. Virgo finds deep satisfaction in being useful, solving problems, and making things work better. However, their critical nature can sometimes turn inward, leading to excessive self-doubt and anxiety.

Career excellence comes in healthcare, accounting, research, editing, quality control, data analysis, nutrition, and environmental science. Virgo thrives in roles that demand precision, analysis, and attention to detail.

Health-wise, Virgo should watch for digestive issues, anxiety, and stress-related ailments. Their tendency to worry can manifest as physical symptoms. Regular meals, adequate sleep, and learning to accept imperfection are essential for their wellbeing.""",
        "strengths_hi": "विश्लेषक, मेहनती, व्यवस्थित, विश्वसनीय, सेवाभावी",
        "strengths_en": "Analytical, hardworking, organized, reliable, helpful",
        "weaknesses_hi": "आलोचनात्मक, चिंताग्रस्त, पूर्णतावादी, अतिविश्लेषक, शर्मीला",
        "weaknesses_en": "Critical, anxious, perfectionist, overthinking, shy",
        "love_hi": "कन्या राशि प्रेम में व्यावहारिक और समर्पित होती है। ये प्यार को बड़े-बड़े इशारों से नहीं बल्कि छोटी-छोटी देखभाल से व्यक्त करते हैं। वृषभ और मकर राशि के साथ सबसे स्थिर और सुखद रिश्ता बनता है।",
        "love_en": "Virgo shows love through acts of service — remembering your coffee order, organizing your desk, noticing when you're unwell. They may not be the most expressive romantics, but their love runs deep and steady. Best matches are Taurus and Capricorn — earth signs who value loyalty and consistency.",
    },
    {
        "id": "tula", "file": "tula.html",
        "hi": "तुला", "en": "Libra", "sym": "Li",
        "dates_hi": "23 सितम्बर – 22 अक्टूबर", "dates_en": "September 23 – October 22",
        "element_hi": "वायु", "element_en": "Air", "ruler_hi": "शुक्र", "ruler_en": "Venus",
        "quality_hi": "चर (Cardinal)", "quality_en": "Cardinal",
        "lucky_day_hi": "शुक्रवार", "lucky_day_en": "Friday",
        "lucky_gem_hi": "ओपल/हीरा", "lucky_gem_en": "Opal / Diamond",
        "lucky_color_hi": "सफ़ेद, हल्का नीला", "lucky_color_en": "White, Light Blue",
        "lucky_num": "6",
        "body_hi": "गुर्दे और कमर", "body_en": "Kidneys and lower back",
        "compatible_hi": "मिथुन, कुम्भ, सिंह", "compatible_en": "Gemini, Aquarius, Leo",
        "incompatible_hi": "कर्क, मकर", "incompatible_en": "Cancer, Capricorn",
        "famous": "अमिताभ बच्चन, महात्मा गाँधी, किम कार्दशियन, रनबीर कपूर",
        "personality_hi": """तुला राशि के जातक संतुलन, सामंजस्य और न्याय के पक्षधर होते हैं। शुक्र ग्रह के स्वामित्व में ये सौंदर्यप्रेमी, कूटनीतिक और मिलनसार होते हैं। इनका जीवन का मूल सिद्धांत है — हर चीज़ में संतुलन।

ये उत्कृष्ट मध्यस्थ होते हैं और किसी भी विवाद को शांतिपूर्वक सुलझा सकते हैं। हालांकि निर्णय लेने में इन्हें कठिनाई होती है क्योंकि ये हर पक्ष को समान रूप से देखते हैं।

करियर में ये कानून, कूटनीति, फ़ैशन, कला, जनसंपर्क और परामर्श में सफल होते हैं। जहाँ भी सौंदर्य बोध और संतुलित दृष्टिकोण की आवश्यकता है, तुला राशि वहाँ उपयुक्त है।

स्वास्थ्य में गुर्दे, कमर दर्द और त्वचा संबंधी समस्याएं हो सकती हैं। पर्याप्त पानी पीना और तनाव मुक्त रहना इनके लिए आवश्यक है।""",
        "personality_en": """Libra is the diplomat of the zodiac — fair, harmonious, and aesthetically inclined. Ruled by Venus, they have an innate sense of beauty and justice that guides everything they do. Balance isn't just their symbol — it's their life philosophy.

They are exceptional mediators who can see every side of an argument. This makes them valued in any social or professional setting. However, their desire to please everyone can lead to indecisiveness and difficulty setting boundaries.

Ideal careers include law, diplomacy, fashion, art, interior design, public relations, counseling, and beauty industry. Libra excels wherever aesthetic sensibility meets interpersonal skill.

Health considerations include kidney issues, lower back pain, and skin conditions. Libra should prioritize hydration, stress management, and maintaining work-life balance — appropriately enough for the sign of the Scales.""",
        "strengths_hi": "संतुलित, कूटनीतिक, कलाप्रेमी, सहयोगी, निष्पक्ष",
        "strengths_en": "Balanced, diplomatic, artistic, cooperative, fair-minded",
        "weaknesses_hi": "अनिर्णायक, टालमटोल, टकराव से बचना, अनुग्रह-प्रिय, आत्मदया",
        "weaknesses_en": "Indecisive, avoidant, conflict-averse, people-pleasing, self-pitying",
        "love_hi": "तुला राशि प्रेम में साझेदारी और सामंजस्य चाहती है। ये रोमांटिक, चतुर और अपने साथी को खुश रखने वाले होते हैं। मिथुन और कुम्भ राशि के साथ इनकी सबसे अच्छी ट्यूनिंग होती है।",
        "love_en": "Libra is the true romantic of the zodiac — they believe in partnership, fairness, and creating beauty together. They are attentive, charming, and genuinely invested in their partner's happiness. Best matches are Gemini and Aquarius — air signs who value intellectual connection and social harmony.",
    },
    {
        "id": "vrishchik", "file": "vrishchik.html",
        "hi": "वृश्चिक", "en": "Scorpio", "sym": "Sc",
        "dates_hi": "23 अक्टूबर – 21 नवम्बर", "dates_en": "October 23 – November 21",
        "element_hi": "जल", "element_en": "Water", "ruler_hi": "मंगल", "ruler_en": "Mars (Pluto)",
        "quality_hi": "स्थिर (Fixed)", "quality_en": "Fixed",
        "lucky_day_hi": "मंगलवार", "lucky_day_en": "Tuesday",
        "lucky_gem_hi": "मूंगा (Red Coral)", "lucky_gem_en": "Red Coral (Moonga)",
        "lucky_color_hi": "गहरा लाल, मैरून", "lucky_color_en": "Maroon, Dark Red",
        "lucky_num": "9",
        "body_hi": "प्रजनन अंग", "body_en": "Reproductive system",
        "compatible_hi": "कर्क, मीन, कन्या", "compatible_en": "Cancer, Pisces, Virgo",
        "incompatible_hi": "सिंह, कुम्भ", "incompatible_en": "Leo, Aquarius",
        "famous": "ऐश्वर्या राय, विराट कोहली, शाहरुख़ ख़ान, स्कारलेट जोहानसन",
        "personality_hi": """वृश्चिक राशि के जातक गहन, रहस्यमयी और दृढ़ निश्चयी होते हैं। मंगल ग्रह के प्रभाव से इनमें अपार शक्ति और तीव्र भावनाएं होती हैं। ये सतह के नीचे छिपी सच्चाई को खोजने में माहिर हैं।

इनकी सबसे बड़ी शक्ति उनकी एकाग्रता और दृढ़ता है। जब ये कोई लक्ष्य निर्धारित करते हैं तो उसे प्राप्त करके ही रहते हैं। विश्वासघात इनके लिए क्षमा करना सबसे कठिन है।

करियर में ये अनुसंधान, चिकित्सा, जासूसी, मनोविज्ञान, शेयर बाज़ार और खनन में उत्कृष्ट होते हैं। गहराई से काम करने वाले हर क्षेत्र में वृश्चिक राशि सफल होती है।

स्वास्थ्य में प्रजनन तंत्र, मूत्र पथ और हार्मोनल असंतुलन की समस्या हो सकती है।""",
        "personality_en": """Scorpio is the most intense sign of the zodiac — deep, mysterious, and powerfully determined. Ruled by Mars (and Pluto in Western astrology), they possess an emotional depth and psychological insight that few other signs can match. They see through pretense instantly.

Their greatest strength is their laser-like focus and unwavering determination. When a Scorpio sets a goal, nothing can deter them. Betrayal is the one thing they find nearly impossible to forgive — their trust, once broken, is rarely restored.

Career excellence comes in research, medicine, detective work, psychology, surgery, financial investigation, mining, and crisis management. Scorpio thrives in any field that requires depth, secrecy, and transformative power.

Health considerations include reproductive health, urinary tract issues, and hormonal imbalances. Emotional suppression can manifest as physical ailments. Regular emotional release through trusted relationships or therapy is vital.""",
        "strengths_hi": "दृढ़ निश्चयी, साहसी, गहन, वफ़ादार, शोधकर्ता",
        "strengths_en": "Determined, brave, deep, loyal, resourceful",
        "weaknesses_hi": "ईर्ष्यालु, रहस्यमयी, प्रतिशोधी, अविश्वासी, अधिकार-भाव",
        "weaknesses_en": "Jealous, secretive, vengeful, distrustful, possessive",
        "love_hi": "वृश्चिक राशि प्रेम में पूर्ण और गहन समर्पण चाहती है। इनके लिए प्रेम सतही आकर्षण नहीं बल्कि आत्मा का मिलन है। कर्क और मीन राशि से सबसे गहरा जुड़ाव होता है।",
        "love_en": "Scorpio loves with consuming intensity. For them, love is not casual — it's a soul-deep merger. They demand complete honesty and loyalty, and offer the same in return. Best matches are Cancer and Pisces — water signs who can navigate their emotional depths.",
    },
    {
        "id": "dhanu", "file": "dhanu.html",
        "hi": "धनु", "en": "Sagittarius", "sym": "Sa",
        "dates_hi": "22 नवम्बर – 21 दिसम्बर", "dates_en": "November 22 – December 21",
        "element_hi": "अग्नि", "element_en": "Fire", "ruler_hi": "गुरु (बृहस्पति)", "ruler_en": "Jupiter",
        "quality_hi": "द्विस्वभाव (Mutable)", "quality_en": "Mutable",
        "lucky_day_hi": "गुरुवार", "lucky_day_en": "Thursday",
        "lucky_gem_hi": "पुखराज (Yellow Sapphire)", "lucky_gem_en": "Yellow Sapphire (Pukhraj)",
        "lucky_color_hi": "पीला, बैंगनी", "lucky_color_en": "Yellow, Purple",
        "lucky_num": "3",
        "body_hi": "जांघ और यकृत", "body_en": "Thighs and liver",
        "compatible_hi": "मेष, सिंह, तुला", "compatible_en": "Aries, Leo, Libra",
        "incompatible_hi": "कन्या, मीन", "incompatible_en": "Virgo, Pisces",
        "famous": "राजनीकांत, ब्रूस ली, टेलर स्विफ्ट, ब्रैड पिट",
        "personality_hi": """धनु राशि के जातक आशावादी, साहसिक और ज्ञान के प्रेमी होते हैं। गुरु ग्रह के स्वामित्व में ये भाग्यशाली, उदार और दार्शनिक प्रवृत्ति के होते हैं। यात्रा और नए अनुभव इनके जीवन का अभिन्न हिस्सा हैं।

ये स्वतंत्रता प्रेमी हैं — बंधन और सीमाएं इन्हें असहज करती हैं। इनकी सोच विशाल और दूरदर्शी होती है। हालांकि कभी-कभी ये अत्यधिक आशावादी हो जाते हैं और ज़मीनी हक़ीक़त से दूर हो सकते हैं।

करियर में ये शिक्षा, कानून, पर्यटन, प्रकाशन, दर्शनशास्त्र और अंतरराष्ट्रीय व्यापार में सफल होते हैं। जहाँ भी विस्तार और खोज की गुंजाइश हो, वहाँ धनु राशि फलती-फूलती है।

स्वास्थ्य में यकृत, जांघ और कूल्हों की समस्या हो सकती है। अत्यधिक भोजन और शराब से बचना आवश्यक है।""",
        "personality_en": """Sagittarius is the adventurer of the zodiac — optimistic, freedom-loving, and eternally curious about life's big questions. Ruled by Jupiter, the planet of expansion and luck, they seem to have a natural good fortune that carries them through even the toughest situations.

They are the travelers, philosophers, and truth-seekers of the zodiac. Their mind ranges across cultures, religions, and ideas with equal enthusiasm. However, their love of freedom can make them commitment-averse and sometimes tactlessly blunt.

Ideal careers include education, law, travel industry, publishing, philosophy, international trade, and motivational speaking. Sagittarius needs a career with room to grow, explore, and share knowledge.

Health-wise, liver health, hip and thigh injuries, and overindulgence are their main concerns. Moderation is the key lesson for this sign that tends to do everything in excess.""",
        "strengths_hi": "आशावादी, उदार, साहसिक, दार्शनिक, हास्यप्रिय",
        "strengths_en": "Optimistic, generous, adventurous, philosophical, humorous",
        "weaknesses_hi": "अधीर, लापरवाह, अति-आशावादी, प्रतिबद्धता से भय, कटुभाषी",
        "weaknesses_en": "Impatient, careless, overconfident, commitment-phobic, tactless",
        "love_hi": "धनु राशि प्रेम में स्वतंत्रता और साहस चाहती है। ये ऐसे साथी की तलाश में रहते हैं जो इनकी यात्रा में साथ चल सके। मेष और सिंह राशि के साथ इनकी सबसे ज़बरदस्त जोड़ी बनती है।",
        "love_en": "Sagittarius seeks a partner who is also a best friend and travel companion. They value freedom within a relationship and need a partner who shares their love of adventure. Best matches are Aries and Leo — fire signs who match their energy and enthusiasm for life.",
    },
    {
        "id": "makar", "file": "makar.html",
        "hi": "मकर", "en": "Capricorn", "sym": "Cp",
        "dates_hi": "22 दिसम्बर – 19 जनवरी", "dates_en": "December 22 – January 19",
        "element_hi": "पृथ्वी", "element_en": "Earth", "ruler_hi": "शनि", "ruler_en": "Saturn",
        "quality_hi": "चर (Cardinal)", "quality_en": "Cardinal",
        "lucky_day_hi": "शनिवार", "lucky_day_en": "Saturday",
        "lucky_gem_hi": "नीलम (Blue Sapphire)", "lucky_gem_en": "Blue Sapphire (Neelam)",
        "lucky_color_hi": "काला, गहरा नीला", "lucky_color_en": "Black, Dark Blue",
        "lucky_num": "8",
        "body_hi": "घुटने और हड्डियाँ", "body_en": "Knees and bones",
        "compatible_hi": "वृषभ, कन्या, मीन", "compatible_en": "Taurus, Virgo, Pisces",
        "incompatible_hi": "मेष, तुला", "incompatible_en": "Aries, Libra",
        "famous": "स्वामी विवेकानंद, ए.आर. रहमान, डेन्ज़ल वॉशिंगटन, विद्या बालन",
        "personality_hi": """मकर राशि के जातक अत्यंत महत्वाकांक्षी, अनुशासित और ज़िम्मेदार होते हैं। शनि ग्रह के प्रभाव से ये धैर्यवान और कठोर परिश्रमी होते हैं। सफलता के लिए ये लंबे समय तक प्रतीक्षा कर सकते हैं।

इनका दृष्टिकोण व्यावहारिक और यथार्थवादी होता है। ये कल्पनाओं में नहीं जीते बल्कि ठोस योजनाएं बनाकर उन पर अमल करते हैं। समय इनका सबसे बड़ा शिक्षक है और उम्र के साथ ये और भी बेहतर होते जाते हैं।

करियर में ये प्रशासन, बैंकिंग, इंजीनियरिंग, वास्तुकला, राजनीति और कॉर्पोरेट प्रबंधन में शीर्ष पर पहुँचते हैं। शनि की कृपा से देर से ही सही, पर सफलता निश्चित मिलती है।

स्वास्थ्य में जोड़ों, घुटनों, हड्डियों और दांतों की समस्या हो सकती है। कैल्शियम युक्त आहार और नियमित व्यायाम अनिवार्य है।""",
        "personality_en": """Capricorn is the achiever of the zodiac — ambitious, disciplined, and built for the long game. Ruled by Saturn, the taskmaster planet, they understand that lasting success requires patience, hard work, and sacrifice. They are willing to climb the mountain step by step while others look for shortcuts.

Their approach to life is practical and realistic. They don't chase dreams — they build plans and execute them methodically. Age is kind to Capricorn; they often become more successful, relaxed, and fulfilled as they grow older.

Career paths that suit Capricorn include administration, banking, engineering, architecture, politics, corporate management, and government. Saturn rewards them with authority and recognition — often later in life, but always substantially.

Health considerations include joint problems, knee issues, bone density, dental health, and depression. Capricorn must guard against overwork and learn that rest is not laziness.""",
        "strengths_hi": "महत्वाकांक्षी, अनुशासित, ज़िम्मेदार, धैर्यवान, व्यावहारिक",
        "strengths_en": "Ambitious, disciplined, responsible, patient, practical",
        "weaknesses_hi": "कठोर, निराशावादी, हठी, भावनाहीन दिखना, अति-कार्यशील",
        "weaknesses_en": "Rigid, pessimistic, stubborn, emotionally cold, workaholic",
        "love_hi": "मकर राशि प्रेम में गंभीर और प्रतिबद्ध होती है। ये दीर्घकालिक साझेदारी चाहते हैं जो समय के साथ और मजबूत हो। वृषभ और कन्या राशि के साथ सबसे स्थिर संबंध बनता है।",
        "love_en": "Capricorn takes love seriously. They seek long-term partnerships built on mutual respect, shared goals, and growing together over time. Best matches are Taurus and Virgo — earth signs who share their values of loyalty, stability, and building something lasting.",
    },
    {
        "id": "kumbh", "file": "kumbh.html",
        "hi": "कुम्भ", "en": "Aquarius", "sym": "Aq",
        "dates_hi": "20 जनवरी – 18 फरवरी", "dates_en": "January 20 – February 18",
        "element_hi": "वायु", "element_en": "Air", "ruler_hi": "शनि", "ruler_en": "Saturn (Uranus)",
        "quality_hi": "स्थिर (Fixed)", "quality_en": "Fixed",
        "lucky_day_hi": "शनिवार", "lucky_day_en": "Saturday",
        "lucky_gem_hi": "नीलम (Blue Sapphire)", "lucky_gem_en": "Blue Sapphire (Neelam)",
        "lucky_color_hi": "नीला, काला", "lucky_color_en": "Blue, Black",
        "lucky_num": "4",
        "body_hi": "टखना और रक्त संचार", "body_en": "Ankles and circulation",
        "compatible_hi": "मिथुन, तुला, धनु", "compatible_en": "Gemini, Libra, Sagittarius",
        "incompatible_hi": "वृषभ, वृश्चिक", "incompatible_en": "Taurus, Scorpio",
        "famous": "अभिषेक बच्चन, ओपरा विन्फ़्रे, क्रिस्टियानो रोनाल्डो, प्रीति ज़िंटा",
        "personality_hi": """कुम्भ राशि के जातक नवीन विचारक, स्वतंत्र और मानवतावादी होते हैं। शनि ग्रह के प्रभाव से ये अपने सिद्धांतों पर अडिग रहते हैं और समाज के कल्याण के लिए सोचते हैं। ये अपने समय से आगे की सोच रखते हैं।

इनका दृष्टिकोण अनोखा और कभी-कभी विद्रोही होता है। ये भीड़ का हिस्सा बनने से इनकार करते हैं और अपना रास्ता स्वयं बनाते हैं। तकनीक और विज्ञान इनकी प्रमुख रुचियां हैं।

करियर में ये तकनीक, विज्ञान, सामाजिक कार्य, आविष्कार, ज्योतिष और जनसेवा में उत्कृष्ट होते हैं। जहाँ भी नवाचार और मानवता की सेवा है, वहाँ कुम्भ राशि अपना योगदान देती है।

स्वास्थ्य में रक्त संचार, टखनों और तंत्रिका तंत्र की समस्या हो सकती है।""",
        "personality_en": """Aquarius is the visionary of the zodiac — innovative, independent, and deeply humanitarian. Ruled by Saturn (and Uranus in Western astrology), they march to the beat of their own drum and often think decades ahead of their time. They are the inventors, reformers, and revolutionaries.

Their perspective is unique and sometimes radical. Aquarius refuses to follow the crowd — they create new paths instead. Technology, science, and social progress fascinate them. However, their intellectualism can sometimes make them seem emotionally detached.

Ideal careers include technology, science, social work, invention, astrology, humanitarian organizations, and anything involving innovation. Aquarius needs a career that lets them change the world in their own unique way.

Health considerations include circulation problems, ankle injuries, and nervous system issues. Their tendency to live in their head means they sometimes neglect physical health.""",
        "strengths_hi": "नवीन, स्वतंत्र, मानवतावादी, बुद्धिमान, मौलिक",
        "strengths_en": "Innovative, independent, humanitarian, intelligent, original",
        "weaknesses_hi": "भावनात्मक रूप से दूर, विद्रोही, अप्रत्याशित, हठी, वैरागी",
        "weaknesses_en": "Emotionally detached, rebellious, unpredictable, stubborn, aloof",
        "love_hi": "कुम्भ राशि प्रेम में बौद्धिक और मैत्रीपूर्ण जुड़ाव चाहती है। ये पहले मित्रता फिर प्रेम में विश्वास करते हैं। मिथुन और तुला राशि के साथ सबसे अच्छी समझ होती है।",
        "love_en": "Aquarius approaches love intellectually first and emotionally second. They need friendship as the foundation of any romantic relationship. Best matches are Gemini and Libra — air signs who stimulate their mind and respect their need for independence.",
    },
    {
        "id": "meen", "file": "meen.html",
        "hi": "मीन", "en": "Pisces", "sym": "Pi",
        "dates_hi": "19 फरवरी – 20 मार्च", "dates_en": "February 19 – March 20",
        "element_hi": "जल", "element_en": "Water", "ruler_hi": "गुरु (बृहस्पति)", "ruler_en": "Jupiter (Neptune)",
        "quality_hi": "द्विस्वभाव (Mutable)", "quality_en": "Mutable",
        "lucky_day_hi": "गुरुवार", "lucky_day_en": "Thursday",
        "lucky_gem_hi": "पुखराज (Yellow Sapphire)", "lucky_gem_en": "Yellow Sapphire (Pukhraj)",
        "lucky_color_hi": "पीला, सफ़ेद", "lucky_color_en": "Yellow, White",
        "lucky_num": "3",
        "body_hi": "पैर और प्रतिरक्षा तंत्र", "body_en": "Feet and immune system",
        "compatible_hi": "कर्क, वृश्चिक, वृषभ", "compatible_en": "Cancer, Scorpio, Taurus",
        "incompatible_hi": "मिथुन, धनु", "incompatible_en": "Gemini, Sagittarius",
        "famous": "आमिर ख़ान, रिहाना, आइंस्टीन, श्रद्धा कपूर",
        "personality_hi": """मीन राशि के जातक अत्यंत कल्पनाशील, दयालु और अंतर्ज्ञानी होते हैं। गुरु ग्रह के प्रभाव से ये आध्यात्मिक प्रवृत्ति के होते हैं और दूसरों की पीड़ा को अपनी पीड़ा मानते हैं। कला और रचनात्मकता इनके रक्त में बहती है।

ये स्वप्नदर्शी हैं — इनकी कल्पना की उड़ान असीमित है। हालांकि कभी-कभी ये यथार्थ से दूर हो जाते हैं और अपनी ही दुनिया में खो जाते हैं। भावनात्मक संवेदनशीलता इनकी शक्ति भी है और कमज़ोरी भी।

करियर में ये कला, संगीत, चिकित्सा, आध्यात्मिकता, फ़ोटोग्राफ़ी, फ़िल्म निर्माण और सामाजिक सेवा में अद्वितीय होते हैं। जहाँ भी सृजनात्मकता और करुणा की ज़रूरत है, मीन राशि वहाँ अपनी छाप छोड़ती है।

स्वास्थ्य में पैरों, प्रतिरक्षा तंत्र और नींद संबंधी समस्याएं हो सकती हैं। नशीले पदार्थों से दूरी और पर्याप्त आराम अत्यंत आवश्यक है।""",
        "personality_en": """Pisces is the dreamer of the zodiac — imaginative, compassionate, and deeply intuitive. Ruled by Jupiter (and Neptune in Western astrology), they exist partly in this world and partly in a realm of imagination, spirituality, and artistic vision. They feel everything deeply — both their own emotions and those of everyone around them.

Their empathy is their greatest gift. Pisces can understand suffering in a way that other signs simply cannot, making them natural healers, artists, and spiritual guides. However, this same sensitivity can lead to escapism and difficulty dealing with harsh realities.

Ideal careers include art, music, healing professions, spirituality, photography, filmmaking, charity work, and marine biology. Pisces needs a career that feeds their soul, not just their bank account.

Health considerations include foot problems, immune system weakness, and sleep disorders. Pisces must be cautious with substances — they have a lower tolerance and higher susceptibility to addiction than most signs.""",
        "strengths_hi": "कल्पनाशील, दयालु, अंतर्ज्ञानी, कलात्मक, आध्यात्मिक",
        "strengths_en": "Imaginative, compassionate, intuitive, artistic, spiritual",
        "weaknesses_hi": "पलायनवादी, अव्यावहारिक, अतिसंवेदनशील, आलसी, बलिदानी",
        "weaknesses_en": "Escapist, impractical, oversensitive, lazy, martyr complex",
        "love_hi": "मीन राशि प्रेम में पूर्ण समर्पण और आत्मिक जुड़ाव चाहती है। ये अत्यंत रोमांटिक और स्वप्निल प्रेमी होते हैं। कर्क और वृश्चिक राशि के साथ सबसे गहरा और सार्थक संबंध बनता है।",
        "love_en": "Pisces loves unconditionally and with their entire soul. They are the most romantic sign, creating a fairy-tale quality in their relationships. They seek a soulmate, not just a partner. Best matches are Cancer and Scorpio — water signs who match their emotional depth and appreciate their tender heart.",
    },
]

ZODIAC_SVG = {
    "mesh": '<svg viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20 C4 12, 8 4, 12 4 C16 4, 20 12, 20 20"/><path d="M12 4 L12 20"/></svg>',
    "vrishabh": '<svg viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="15" r="6"/><path d="M6 9 C6 5, 9 3, 12 5 C15 3, 18 5, 18 9"/></svg>',
    "mithun": '<svg viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M6 4 C9 6, 15 6, 18 4"/><path d="M6 20 C9 18, 15 18, 18 20"/><line x1="8" y1="5" x2="8" y2="19"/><line x1="16" y1="5" x2="16" y2="19"/></svg>',
    "kark": '<svg viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="8" cy="10" r="3"/><circle cx="16" cy="14" r="3"/><path d="M11 10 C14 6, 20 8, 19 14"/><path d="M13 14 C10 18, 4 16, 5 10"/></svg>',
    "singh": '<svg viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="16" r="4"/><path d="M13 16 C13 10, 18 6, 18 10 C18 14, 14 14, 14 10 C14 6, 8 4, 6 8"/></svg>',
    "kanya": '<svg viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4 L4 18 C4 20, 6 20, 6 18 L6 4"/><path d="M6 4 L6 18 C6 20, 8 20, 8 18 L8 4"/><path d="M8 4 L8 14 C8 18, 12 20, 14 16"/><path d="M14 16 C16 12, 20 14, 18 18"/></svg>',
    "tula": '<svg viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="18" x2="20" y2="18"/><line x1="4" y1="14" x2="20" y2="14"/><path d="M7 14 C7 8, 12 5, 17 14"/></svg>',
    "vrishchik": '<svg viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4 L4 18 C4 20, 6 20, 6 18 L6 4"/><path d="M6 4 L6 18 C6 20, 8 20, 8 18 L8 4"/><path d="M8 4 L8 18 C8 20, 10 20, 12 18 L16 14"/><path d="M14 12 L16 14 L14 16"/></svg>',
    "dhanu": '<svg viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="20" x2="20" y2="4"/><path d="M14 4 L20 4 L20 10"/><line x1="8" y1="12" x2="16" y2="12" transform="rotate(-45 12 12)"/></svg>',
    "makar": '<svg viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4 L4 14 C4 18, 8 20, 10 16 L10 10"/><path d="M10 10 C10 14, 14 18, 18 18 C20 18, 20 14, 18 12 C16 10, 18 8, 20 8"/></svg>',
    "kumbh": '<svg viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 10 C6 8, 8 12, 10 10 C12 8, 14 12, 16 10 C18 8, 20 12, 20 10"/><path d="M4 16 C6 14, 8 18, 10 16 C12 14, 14 18, 16 16 C18 14, 20 18, 20 16"/></svg>',
    "meen": '<svg viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6 C10 10, 10 14, 4 18"/><path d="M20 6 C14 10, 14 14, 20 18"/><line x1="4" y1="12" x2="20" y2="12"/></svg>',
}

NAV_LINKS = [
    ("Rashifal", "index.html"),
    ("Horoscopes", "index.html#horoscopes"),
    ("Compatibility", "index.html#compatibility"),
    ("Tools", "index.html#tools"),
    ("Zodiac", "index.html#zodiac"),
]

# Adjacent rashis for prev/next navigation
def get_adjacent(idx):
    prev_idx = (idx - 1) % 12
    next_idx = (idx + 1) % 12
    return RASHIS[prev_idx], RASHIS[next_idx]


def generate_page(rashi, idx):
    prev_r, next_r = get_adjacent(idx)
    svg = ZODIAC_SVG[rashi["id"]]

    html = f"""<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{rashi['hi']} राशिफल | {rashi['en']} Horoscope — Rashifal.online</title>
<meta name="description" content="{rashi['hi']} ({rashi['en']}) राशिफल — आज का भविष्यफल, व्यक्तित्व, करियर, प्रेम, स्वास्थ्य। {rashi['en']} daily horoscope, personality, career, love, health predictions.">
<meta name="keywords" content="{rashi['hi']} rashifal, {rashi['en'].lower()} horoscope, {rashi['id']} rashifal, {rashi['hi']} राशिफल आज">
<link rel="canonical" href="https://rashifal.online/{rashi['file']}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@300;400;500;600&family=Tiro+Devanagari+Hindi:ital@0;1&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{margin:0;padding:0;box-sizing:border-box}}
:root{{
  --midnight:#0A0E1A;--charcoal:#131825;--gold:#D4AF37;--gold-light:#E8CC6E;
  --gold-muted:rgba(212,175,55,0.12);--gold-faint:rgba(212,175,55,0.03);
  --t-heading:rgba(232,228,218,0.95);--t-body:rgba(200,205,220,0.82);
  --t-muted:rgba(200,205,220,0.62);--t-faint:rgba(200,205,220,0.36);
  --b-subtle:rgba(212,175,55,0.06);--b-default:rgba(212,175,55,0.1);
  --f-serif:'Cormorant Garamond','Tiro Devanagari Hindi',Georgia,serif;
  --f-sans:'Inter',system-ui,sans-serif;--f-hindi:'Tiro Devanagari Hindi',serif;
  --glass-bg:rgba(14,18,30,0.55);--glass-blur:blur(16px);--glass-border:1px solid rgba(255,255,255,0.04);
  --glass-radius:14px;
}}
html{{scroll-behavior:smooth;font-size:16px}}
body{{background:var(--midnight);color:var(--t-body);font-family:var(--f-sans);line-height:1.7;min-height:100vh;-webkit-font-smoothing:antialiased}}
h1,h2,h3,h4{{font-family:var(--f-serif);color:var(--t-heading);font-weight:600;line-height:1.2}}
.container{{max-width:860px;margin:0 auto;padding:0 1.5rem}}

/* Nav */
.nav{{position:sticky;top:0;z-index:50;background:rgba(7,11,20,0.85);backdrop-filter:var(--glass-blur);border-bottom:1px solid var(--b-subtle)}}
.nav-inner{{max-width:1120px;margin:0 auto;padding:0 1.5rem;display:flex;align-items:center;height:56px;gap:0.5rem}}
.nav-brand{{font-family:var(--f-serif);font-size:1.333rem;font-weight:600;color:var(--gold);text-decoration:none;margin-right:auto}}
.nav-brand:hover{{color:var(--gold-light)}}
.nav-link{{padding:0.5rem 1rem;font-size:0.875rem;font-weight:500;color:var(--t-muted);text-decoration:none;border-radius:6px;transition:color 0.2s}}
.nav-link:hover{{color:var(--t-heading)}}
.nav-links{{display:flex;gap:0.25rem}}

/* Hero */
.hero{{text-align:center;padding:4rem 0 3rem}}
.hero-icon{{width:80px;height:80px;border-radius:50%;border:1.5px solid rgba(212,175,55,0.2);display:inline-flex;align-items:center;justify-content:center;margin-bottom:1.5rem}}
.hero-icon svg{{width:40px;height:40px}}
.hero h1{{font-size:clamp(1.777rem,4vw,2.369rem);color:var(--gold);margin-bottom:0.25rem}}
.hero .sub{{font-size:0.875rem;color:var(--t-muted);text-transform:uppercase;letter-spacing:3px}}
.hero .dates{{font-size:1rem;color:var(--t-muted);margin-top:0.75rem}}

/* Card */
.card{{background:var(--glass-bg);backdrop-filter:var(--glass-blur);border:var(--glass-border);border-radius:var(--glass-radius);padding:2rem;margin-bottom:1.5rem}}
.card h2{{font-size:1.333rem;margin-bottom:1rem;color:var(--gold-light)}}
.card h3{{font-size:1.1rem;margin-bottom:0.75rem;color:var(--gold-light)}}

/* Info grid */
.info-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:1rem;margin:1.5rem 0}}
.info-item{{background:rgba(255,255,255,0.03);border-radius:10px;padding:1rem;text-align:center}}
.info-label{{font-size:0.75rem;color:var(--t-faint);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:0.25rem}}
.info-value{{font-family:var(--f-serif);font-size:1.1rem;color:var(--gold)}}

/* Prose */
.prose{{font-size:1rem;line-height:1.85;color:var(--t-body)}}
.prose.hi{{font-family:var(--f-hindi);line-height:1.95}}
.prose p{{margin-bottom:1rem}}

/* Tags */
.tags{{display:flex;flex-wrap:wrap;gap:0.5rem;margin:1rem 0}}
.tag{{padding:0.25rem 0.75rem;border-radius:4px;font-size:0.75rem;font-weight:500;letter-spacing:0.5px}}
.tag-pos{{background:rgba(74,191,138,0.1);color:#4abf8a;border:1px solid rgba(74,191,138,0.15)}}
.tag-neg{{background:rgba(212,99,138,0.1);color:#d4638a;border:1px solid rgba(212,99,138,0.15)}}

/* Today's prediction */
.prediction-card{{background:linear-gradient(135deg,rgba(212,175,55,0.04),rgba(14,18,30,0.6));border:1px solid rgba(212,175,55,0.08);border-radius:var(--glass-radius);padding:2rem;margin:1.5rem 0}}
.prediction-card h2{{color:var(--gold)}}
.pred-meta{{display:flex;gap:1.5rem;flex-wrap:wrap;margin-top:1rem}}
.pred-meta-item{{font-size:0.875rem;color:var(--t-muted)}}
.pred-meta-item span{{color:var(--gold);font-weight:500}}

/* Nav prev/next */
.rashi-nav{{display:flex;justify-content:space-between;padding:2rem 0;border-top:1px solid var(--b-subtle);margin-top:2rem}}
.rashi-nav a{{font-family:var(--f-serif);font-size:1rem;color:var(--t-muted);text-decoration:none;transition:color 0.2s}}
.rashi-nav a:hover{{color:var(--gold)}}

/* Footer */
footer{{text-align:center;padding:3rem 1.5rem 2rem;border-top:1px solid var(--b-subtle);margin-top:2rem;color:var(--t-faint);font-size:0.875rem}}
footer a{{color:var(--gold);text-decoration:none}}

/* Back to top */
.back-link{{display:inline-block;margin:2rem 0;font-size:0.875rem;color:var(--t-muted);text-decoration:none;transition:color 0.2s}}
.back-link:hover{{color:var(--gold)}}

/* Responsive */
@media(max-width:768px){{
  .nav-links{{display:none}}
  .info-grid{{grid-template-columns:1fr 1fr}}
  .hero{{padding:2.5rem 0 2rem}}
  .card{{padding:1.5rem}}
}}

/* Lang toggle */
.lang-sw{{display:flex;border:1px solid var(--b-default);border-radius:6px;overflow:hidden;margin:1rem auto;width:fit-content}}
.lang-b{{padding:0.4rem 1.25rem;font-size:0.875rem;font-weight:500;background:none;border:none;color:var(--t-muted);cursor:pointer;font-family:var(--f-sans);transition:all 0.2s}}
.lang-b.active{{background:var(--gold-muted);color:var(--gold)}}
.en-only{{display:none}}.hi-only{{display:block}}
body.lang-en .en-only{{display:block}}body.lang-en .hi-only{{display:none}}
</style>
</head>
<body>

<nav class="nav"><div class="nav-inner">
  <a href="index.html" class="nav-brand">Rashifal</a>
  <div class="nav-links">
    <a href="index.html" class="nav-link">Home</a>
    <a href="index.html#horoscopes" class="nav-link">Horoscopes</a>
    <a href="index.html#compatibility" class="nav-link">Compatibility</a>
    <a href="index.html#zodiac" class="nav-link">Zodiac</a>
  </div>
</div></nav>

<div class="container">

  <div class="lang-sw">
    <button class="lang-b active" onclick="setL('hi')">हिन्दी</button>
    <button class="lang-b" onclick="setL('en')">English</button>
  </div>

  <div class="hero">
    <div class="hero-icon">{svg}</div>
    <h1 class="hi-only">{rashi['hi']} राशिफल</h1>
    <h1 class="en-only">{rashi['en']} Horoscope</h1>
    <div class="sub">{rashi['en']} &middot; {rashi['element_en']} &middot; {rashi['ruler_en']}</div>
    <div class="dates hi-only">{rashi['dates_hi']}</div>
    <div class="dates en-only">{rashi['dates_en']}</div>
  </div>

  <!-- Today's Prediction -->
  <div class="prediction-card" id="todayPred">
    <h2 class="hi-only">आज का {rashi['hi']} राशिफल</h2>
    <h2 class="en-only">Today's {rashi['en']} Horoscope</h2>
    <div class="prose hi-only" id="predHi"><p>राशिफल लोड हो रहा है...</p></div>
    <div class="prose en-only" id="predEn"><p>Loading prediction...</p></div>
    <div class="pred-meta" id="predMeta"></div>
  </div>

  <!-- Quick Facts -->
  <div class="info-grid">
    <div class="info-item"><div class="info-label hi-only">तत्व</div><div class="info-label en-only">Element</div><div class="info-value hi-only">{rashi['element_hi']}</div><div class="info-value en-only">{rashi['element_en']}</div></div>
    <div class="info-item"><div class="info-label hi-only">स्वामी ग्रह</div><div class="info-label en-only">Ruler</div><div class="info-value hi-only">{rashi['ruler_hi']}</div><div class="info-value en-only">{rashi['ruler_en']}</div></div>
    <div class="info-item"><div class="info-label hi-only">शुभ दिन</div><div class="info-label en-only">Lucky Day</div><div class="info-value hi-only">{rashi['lucky_day_hi']}</div><div class="info-value en-only">{rashi['lucky_day_en']}</div></div>
    <div class="info-item"><div class="info-label hi-only">शुभ रत्न</div><div class="info-label en-only">Lucky Gem</div><div class="info-value hi-only">{rashi['lucky_gem_hi']}</div><div class="info-value en-only">{rashi['lucky_gem_en']}</div></div>
    <div class="info-item"><div class="info-label hi-only">शुभ रंग</div><div class="info-label en-only">Lucky Color</div><div class="info-value hi-only">{rashi['lucky_color_hi']}</div><div class="info-value en-only">{rashi['lucky_color_en']}</div></div>
    <div class="info-item"><div class="info-label hi-only">शुभ अंक</div><div class="info-label en-only">Lucky Number</div><div class="info-value">{rashi['lucky_num']}</div></div>
    <div class="info-item"><div class="info-label hi-only">शरीर अंग</div><div class="info-label en-only">Body Part</div><div class="info-value hi-only">{rashi['body_hi']}</div><div class="info-value en-only">{rashi['body_en']}</div></div>
    <div class="info-item"><div class="info-label hi-only">गुण</div><div class="info-label en-only">Quality</div><div class="info-value hi-only">{rashi['quality_hi']}</div><div class="info-value en-only">{rashi['quality_en']}</div></div>
  </div>

  <!-- Personality -->
  <div class="card">
    <h2 class="hi-only">{rashi['hi']} राशि का व्यक्तित्व</h2>
    <h2 class="en-only">{rashi['en']} Personality</h2>
    <div class="prose hi hi-only">{''.join(f'<p>{p.strip()}</p>' for p in rashi['personality_hi'].strip().split(chr(10)+chr(10)) if p.strip())}</div>
    <div class="prose en-only">{''.join(f'<p>{p.strip()}</p>' for p in rashi['personality_en'].strip().split(chr(10)+chr(10)) if p.strip())}</div>
  </div>

  <!-- Strengths & Weaknesses -->
  <div class="card">
    <h2 class="hi-only">गुण और कमज़ोरियाँ</h2>
    <h2 class="en-only">Strengths & Weaknesses</h2>
    <h3 class="hi-only">गुण (Strengths)</h3>
    <h3 class="en-only">Strengths</h3>
    <div class="tags">{''.join(f'<span class="tag tag-pos">{s.strip()}</span>' for s in rashi['strengths_hi'].split(','))}</div>
    <div class="tags en-only" style="display:none">{''.join(f'<span class="tag tag-pos">{s.strip()}</span>' for s in rashi['strengths_en'].split(','))}</div>
    <h3 class="hi-only" style="margin-top:1.5rem">कमज़ोरियाँ (Weaknesses)</h3>
    <h3 class="en-only" style="margin-top:1.5rem">Weaknesses</h3>
    <div class="tags">{''.join(f'<span class="tag tag-neg">{s.strip()}</span>' for s in rashi['weaknesses_hi'].split(','))}</div>
    <div class="tags en-only" style="display:none">{''.join(f'<span class="tag tag-neg">{s.strip()}</span>' for s in rashi['weaknesses_en'].split(','))}</div>
  </div>

  <!-- Love -->
  <div class="card">
    <h2 class="hi-only">{rashi['hi']} राशि और प्रेम</h2>
    <h2 class="en-only">{rashi['en']} in Love</h2>
    <div class="prose hi hi-only"><p>{rashi['love_hi']}</p></div>
    <div class="prose en-only"><p>{rashi['love_en']}</p></div>
    <div style="margin-top:1rem">
      <div class="info-label hi-only" style="margin-bottom:0.5rem">अनुकूल राशियाँ</div>
      <div class="info-label en-only" style="margin-bottom:0.5rem">Compatible Signs</div>
      <div class="hi-only" style="color:var(--gold);font-family:var(--f-serif)">{rashi['compatible_hi']}</div>
      <div class="en-only" style="color:var(--gold);font-family:var(--f-serif)">{rashi['compatible_en']}</div>
      <div class="info-label hi-only" style="margin-top:1rem;margin-bottom:0.5rem">कम अनुकूल</div>
      <div class="info-label en-only" style="margin-top:1rem;margin-bottom:0.5rem">Challenging Matches</div>
      <div class="hi-only" style="color:var(--t-muted)">{rashi['incompatible_hi']}</div>
      <div class="en-only" style="color:var(--t-muted)">{rashi['incompatible_en']}</div>
    </div>
  </div>

  <!-- Famous People -->
  <div class="card">
    <h2 class="hi-only">प्रसिद्ध {rashi['hi']} राशि के व्यक्तित्व</h2>
    <h2 class="en-only">Famous {rashi['en']} Personalities</h2>
    <p style="color:var(--t-body);font-size:1rem">{rashi['famous']}</p>
  </div>

  <!-- Prev / Next -->
  <div class="rashi-nav">
    <a href="{prev_r['file']}">&larr; <span class="hi-only">{prev_r['hi']}</span><span class="en-only">{prev_r['en']}</span></a>
    <a href="index.html" style="color:var(--gold)">All Rashis</a>
    <a href="{next_r['file']}"><span class="hi-only">{next_r['hi']}</span><span class="en-only">{next_r['en']}</span> &rarr;</a>
  </div>

  <a href="index.html" class="back-link">&larr; <span class="hi-only">सभी राशिफल देखें</span><span class="en-only">View all horoscopes</span></a>

</div>

<footer>
  <p>Rashifal.online &middot; 2026 &middot; Bhopal, India</p>
  <p style="margin-top:0.5rem"><a href="privacy.html">Privacy</a> &middot; <a href="terms.html">Terms</a> &middot; <a href="about.html">About</a></p>
</footer>

<script>
function setL(l){{
  document.body.classList.toggle('lang-en',l==='en');
  document.querySelectorAll('.lang-b').forEach(b=>b.classList.toggle('active',b.textContent.includes(l==='hi'?'हिन':'Eng')));
  localStorage.setItem('rashifal_lang',l);
}}
if(localStorage.getItem('rashifal_lang')==='en')setL('en');

// Load today's prediction
(async function(){{
  const today=new Date();
  const y=today.getFullYear(),m=String(today.getMonth()+1).padStart(2,'0'),d=String(today.getDate()).padStart(2,'0');
  const url=`/content/${{y}}-${{m}}-${{d}}.json`;
  try{{
    const r=await fetch(url);
    if(!r.ok)return;
    const data=await r.json();
    const rashi=data.rashis?.find(r=>r.id==='{rashi["id"]}');
    if(!rashi)return;
    if(rashi.hindi){{
      document.getElementById('predHi').innerHTML='<p>'+rashi.hindi.prediction+'</p>';
      const metaH=[];
      if(rashi.hindi.lucky_number)metaH.push('<span class="pred-meta-item hi-only">शुभ अंक: <span>'+rashi.hindi.lucky_number+'</span></span>');
      if(rashi.hindi.lucky_color)metaH.push('<span class="pred-meta-item hi-only">शुभ रंग: <span>'+rashi.hindi.lucky_color+'</span></span>');
      document.getElementById('predMeta').innerHTML+=metaH.join('');
    }}
    if(rashi.english){{
      document.getElementById('predEn').innerHTML='<p>'+rashi.english.prediction+'</p>';
      const metaE=[];
      if(rashi.english.lucky_number)metaE.push('<span class="pred-meta-item en-only">Lucky #: <span>'+rashi.english.lucky_number+'</span></span>');
      if(rashi.english.lucky_color)metaE.push('<span class="pred-meta-item en-only">Color: <span>'+rashi.english.lucky_color+'</span></span>');
      document.getElementById('predMeta').innerHTML+=metaE.join('');
    }}
  }}catch(e){{}}
}})();
</script>

<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"Article",
  "headline":"{rashi['hi']} राशिफल — {rashi['en']} Horoscope",
  "description":"{rashi['en']} daily horoscope and personality traits",
  "url":"https://rashifal.online/{rashi['file']}",
  "inLanguage":["hi","en"],
  "publisher":{{"@type":"Organization","name":"Rashifal.online"}}
}}
</script>
</body>
</html>"""
    return html


# Generate all pages
output_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

for idx, rashi in enumerate(RASHIS):
    filepath = os.path.join(output_dir, rashi["file"])
    html = generate_page(rashi, idx)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  Created: {rashi['file']} ({rashi['hi']} / {rashi['en']})")

# Update sitemap
sitemap_path = os.path.join(output_dir, "sitemap.xml")
urls = ['<url><loc>https://rashifal.online/</loc><changefreq>daily</changefreq><priority>1.0</priority></url>']
for r in RASHIS:
    urls.append(f'<url><loc>https://rashifal.online/{r["file"]}</loc><changefreq>daily</changefreq><priority>0.8</priority></url>')
for page in ["methodology.html","about.html","privacy.html","terms.html","contact.html"]:
    urls.append(f'<url><loc>https://rashifal.online/{page}</loc><changefreq>monthly</changefreq><priority>0.4</priority></url>')

sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/xmlns/sitemap/0.9">
{chr(10).join(urls)}
</urlset>"""
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sitemap)
print(f"  Updated: sitemap.xml ({len(urls)} URLs)")

print("\nDone! All 12 rashi pages + updated sitemap generated.")
