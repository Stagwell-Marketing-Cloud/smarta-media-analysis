from enum import Enum

class EmotionWordsPattern(Enum):
    LOYALTY_TO_BRAND_MISION	= "Cemented"
    LOYALTY_TO_CUSTOMERS = "Caliber"
    CONFIDENCE_IN_CONSUMER = "Achieve"
    FEAR = "Alone"
    ANGER = "Atrocious"
    CURIOSITY = "Bonus"
    URGENCY = "Limited time"
    EXCLUSIVE = "Limited edition"
    TRUST = "Authentic"
    INSPIRE = "Destiny"
    PROVOCATIVE = "Controversial"
    SURPRISE = "Revolutionary"
    INSTANT_GRATIFICATION = "Novelty"
    POSITIVE = "Absolving"

EMOTION_WORDS_PATTERNS = {
    EmotionWordsPattern.LOYALTY_TO_BRAND_MISION: [
        "Cemented","Committed","Consistent","Cornerstone","Countless","Dedicated","Devoted","Embedded","Enduring","Entrenched","Evergreen","Everlasting","For over X years","Hallmark","Ingrained","Longevity","Maintain","Mission","Never","No matter what","Our promise","Our standards","Over the years","Pride ourselves on","Remain","Steadfast","Sustained","Tradition","Uncompromising","Unshakeable ","Bond","Community","Connected","Customer spotlight","Customer success","Evangelists","Family","Frequent flyers","Friends","Gratitude","Have stuck with us","Join X others","Like our own","Long-time","Members","Mutual","Neighbors","Regulars","Relationships","ee why our customers keep returning","Throughout your/our journey","Together","Unwavering"
    ],
    EmotionWordsPattern.LOYALTY_TO_CUSTOMERS: [
        "Caliber","Capable","Count on","Data-backed","Definitive","Deliver | We deliver on our promise of .+.","Depend","[Eliminate problem] for good","Equipped","Every single time","Evidence-based","Experts","Focused","Fool-proof","Forefront","Founded on","Hands-down","Market leader","Most reliable","Only","Pioneers","Proven","Recommended","Rely | [X] small businesses rely on our solutions to [reach desired goal].","Rooted","See who we’ve helped so far","Specialty","Swear by | See why our clients swear by our [solution].","The [company name] difference/advantage","Thorough","Top tier","Top trusted","Tried and true","Trusted by over X","Vetted","Why choose us? [then answer that]","Why [your product/service] beats [a larger competitor’s]","World-class"
    ],
    EmotionWordsPattern.CONFIDENCE_IN_CONSUMER: [
    "Achieve","Available","Become the .+ you’ve always wanted to be.","Belong","Clarity","Compassionate","Doubt no longer","Eliminate the guesswork","Every step","Fear not","From start to finish","Guide","Got your back","Got you covered","In good hands","If you’re like most [members of niche]… (This is better than saying “It’s obvious that” or “Clearly”).","Informed decisions","Master","Meet you where you are","Move the needle","No matter where you’re at","Own your .+","Pull the trigger","Rest assured","Results you want","Say goodbye to","Secure","Sound decisions","Surefooted","Tackle","Take charge of","Take control","The support you need","Tips we swear by","Together we can [accomplish client’s vision]","Under our wing","Uncover the [ability/desired entity] you didn’t know you had","Walk you through","We’ll find a way","You hold the power","You’re not alone"
    ],
    EmotionWordsPattern.FEAR: [
        "Alone","Are you ready/prepared/equipped?","Avoid","Befall","Before it’s too late","Beware","Caution","Cost you","Danger","Decline","Drop","Fail","Fall victim too","Fooled","Helpless","Hurting","Jeopardize","Killing","Lose","Loss","Miss","Mistake","Neglect","Never","Not enough","Pitfalls","Plummet","Prevent [bad outcome]","Preventing | Could your habits be preventing you from achieving [desired outcome]?","Protect your","Powerless","[Don’t] realize","Really  | But are you really moving the needle?","Regret","Rejection","Risk","Sabotage","Scary","Should  | X scary stats every [target customer persona] should be aware of.","Suffer","Steal","Threat","Too late","Tragic","Trapped","Vulnerable","Waste | Are you wasting your time on strategies that don’t work?","Worry","What NOT to do","Why you need to [stop/get rid of] right now","Will you survive"
    ],
    EmotionWordsPattern.ANGER: [
        "Atrocious","Burned","Can’t seem to","Driving you mad","Disappoint","Deal with","Endless","Envy","Fed up with","Fleeced","Frustrated","Greedy","Had enough of","Had it with","Hassle","Hidden","Irritated by","Jealous","Maddening","Ruthless","Never-ending","Reached your limit","Relentless","Misleading","Infuriating","Pointless","Reclaim","Sick and tired","Sick of","Swindled","Trigger","Unacceptable"
    ],
    EmotionWordsPattern.CURIOSITY: [
    "Bonus","Brilliant","Change your mind","Choose your own adventure","Confessions of a","Confidential","Different","Discover","Dramatic","Eye-opening","Fascinating","Favorite","Find out/Find out why","Game-changing","Hidden/hidden gems","It’s not what you think","Jaw-dropping","Lesser-known","Little-known","Life-changing","Mind-blowing","Mind-bending","Must-know","Must-read","Myths","New","No one talks about","Odd","Overlooked","Remarkable","Rethink","Revealed","Revolutionary","Secret","Secret weapon","Shocking","Spoiler","Strange","Teaser","That you didn’t know you needed","That you’ve been waiting for","The last one is our favorite","Things nobody tells you","Truth","Unconventional","Unusual","Wait and see","Weird","What we found","What do you have to lose?","You’ll wish you knew/created/learned sooner","You will never guess","You won’t believe"
    ],
    EmotionWordsPattern.URGENCY: [
        "Limited time","Act now","Deadline","Last time","Don’t delay","Hurry","Never again","Once in a lifetime ","Clearance","Price going up","Final chance","Bargain","While stock last","Units remaining","Offer expires","Quick","Flash sale","Don’t miss out"
    ],
    EmotionWordsPattern.EXCLUSIVE: [
    "Limited edition","Members-only","Restricted access","Join the club","Rare","Once in a lifetime","Insider","Exclusive","Premium","Class full","Only available to subscribers","Be one of the few","Unique","Deadline","Expires","Fast","Final","Hurry","Last Chance","Limited","Never again","New","Now","Quick","Running Out","Elite"
    ],
    EmotionWordsPattern.TRUST: [
        "Authentic","Certified","Guaranteed","Money back","Proven","Genuine","Reviews","Safety","Secure","Endorsed","Unconditional","Refund","Lifetime","Years’ warranty","Verified","No risk","Dependable","Confirmation","Customer reviews","No risk"
    ],
    EmotionWordsPattern.INSPIRE: [
        "Destiny","Empower","How","Overcome","Reclaim","Crush","Seize","Imagine","Discover","Boost","Cure","Fix","Win","Need","Enhance","Build","Inspire","Accelerate","Adapt","Calibrate","Troubleshoot","Strive","Beat","Satisfaction","Peace","Joy","Undo","Glow","Energize","Convert"
    ],
    EmotionWordsPattern.PROVOCATIVE: [
        "Controversial","Stop","Worse","Exposed","Surrender","Craving","Sabotage","Forgotten","Mysterious","Revenge","Failure","Ridiculous","Taboo","Helpless","Destroy"
    ],
    EmotionWordsPattern.SURPRISE: [
        "Revolutionary","Mesmerizing","Mind-blowing","Astonishing","Terrific","Jaw-dropping","Spectacular","Breath-taking","Charming","Amazing","Wonder","Blissful","Remarkable","Vibrant"
    ],
    EmotionWordsPattern.INSTANT_GRATIFICATION: [
        "Novelty","New","Free","Instant","More","Faster","Cheaper","Easy","Want","Never","Yes"
    ],
    EmotionWordsPattern.POSITIVE: [
        "Absolving","Adequate","Admiring","Adores","Agreed","Ambitious","Anguish","Applauded","Appreciated","Appropriate","Awarded","Beautiful","Benefits","Bless","Boastful","Breathtaking","Calm","Capability","Celebrated","Charm","Clarity","Comfort","Commended","Complacent","Congrats","Consolable","Cool","Decisive","Dream","Effectively","Empathetic","Encouragement","Enjoy","Enlightening","Enthusiastic","Exuberant","Favoured","Fondness","Friendly","Glad","Gloomy","Godsend","Gracious","Greatness","Heaven","Honoured","Impatient","Impressive","Indomitable","Innovative","Inspires","Intelligent","Invincible","Kudos","Laughs","Likes","Loved","Mandatory","Masterpieces","Motivate","Nice","Overjoyed","Peaceful","Perfectly","Pleased","Possessive","Praising","Proactive","Prompt","Recommend","Rejoiced","Relentless","Resplendent","Rewarding","Satisfied","Smart","Smiles","Solved","Soothing","Stable","Stunning","Sunshine","Supports","Thank","Tranquil","Underestimate","Vindicating","Warm","Winning","Won","Worthy","Accomplished","Admire","Adorable","Advantage","Amazed","Amuse","Appeased","Applauding","Appreciates","Approved","Awesome","Beautifully","Benefitted","Blesses","Boost","Brightest","Calmed","Capable","Celebrating","Charming","Clean","Comfortable","Compassionate","Comprehensive","Congratulate","Contentious","Creative","Dedicated","Easy","Elegant","Empowerment","Encourages","Enjoying","Enterprising","Entrusted","Fabulous","Favours","Formidable","Funny","Glamorous","Glorious","Good","Grand","Gusto","Heavenly","Honouring","Impress","Improved","Influential","Inspiration","Inspiring","Intense","Irresistible","Laugh","Legal","Lmfao","Lovelies","Marvellous","Meaningful","Motivated","Nifty","Overlooked","Peacefully","Perfects","Pleasure","Praise","Prepared","Profiteer","Proudly","Recommended","Rejoices","Relishing","Responsive","Riches","Saved","Smartest","Smiling","Solves","Sophisticated","Stimulated","Suave","Super","Supreme","Thankful","Treasure","Underestimated","Virtuous","Welcomed","Wins","Woo","Wow","Achievable","Admired","Adore","Advantages","Amazing","Amused","Appeasing","Applauds","Appreciating","Assuredly","Badass","Beautify","Benefitting","Blessing","Bravado","Brightness","Calming","Captivated","Champion","Charmless","Clears","Comforting","Compel","Confidence","Congratulation","Convinced","Cut","Desire","Ecstatic","Elegantly","Enchanted","Energetic","Enjoys","Entertaining","Excellence","Faithful","Fit","Fortunate","Generous","Glamourous","Godlike","Goodness","Gratification","Healthy","Heroic","Hugs","Impressed","Improvement","Innovate","Inspirational","Instruct","Intricate","Justified","Laughed","Lifesaver","Lovable","Lovely","Masterful","Merciless","Motivating","Obsessed","Paradise","Perfect","Playful","Positive","Praised","Pretty","Promise","Provoking","Recommends","Rejoicing","Resolving","Reward","Robust","Sexy","Smile","Solemn","Soothe","Sovereign","Stimulating","Substantial","Superb","Sweet","Thanks","Trusted","Victor","Virulent","Win","Wish","World-famous","Yes","Achievement","Admires","Adored","Agreeable","Amazingly","Amusement","Applaud","Appreciate","Appreciation","Award","Beauties","Beloved","Best","Boast","Brave","Brilliant","Calms","Celebrate","Charges","Cherished","Clever","Commend","Competent","Confident","Congratulations","Convivial","Cute","Distinguished","Effective","Embrace","Encouraged","Engrossed","Enlightened","Enthral","Excellent","Favourite","Focused","Fresh","Genial","Gleeful","Godliness","Grace","Greatest","Heartfelt","Honour","Humorous","Impresses","Indestructible","Innovates","Inspired","Intact","Intrigues","Kiss","Laughing","Liked","Love","Loving","Masterpiece","Miracle","Motivation","Outstanding","Passionate","Perfected","Pleasant","Positively","Praises","Privileged","Promised","Puzzled","Rejoice","Relaxed","Respected","Rewarded","Safe","Sincerity","Smiled","Solid","Soothed","Splendid","Strengthened","Substantially","Supported","Sympathetic","Thoughtful","Undaunted","Victorious","Vivacious","Winner","Wishing","Worth","Youthful"
    ]
}

ALL_EMOTION_WORDS_PHRASES = set().union(*EMOTION_WORDS_PATTERNS.values())


