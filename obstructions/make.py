'''
generate list of obstructions.

TODO: make more natural.
TODO: make proper generator script for better combinations.
TODO: implement a better strategy for ordering this file.
'''
import random

def prog_lang():
    return ("Must use the '{}' programming language.".format(p)
            for p in prog_langs)

prog_langs = [
    "APL", "BASIC", "Forth", "Lisp", "Lua", "Pascal", "Perl", "Python", "Ruby",
    "Erlang", "Swift", "Bash", "F#", "ELixir", "Haskell", "Ada", "ALGOL", "C",
    "Clojure", "Shell Script", "C++", "C#", "SQL", "COBOL", "Fortran", "Java",
    "Objective-C", "Smalltalk", "Visual Basic", "MATLAB", "Occam", "AppleScript",
    "Awk", "ColdFusion", "PHP", "Go", "Rust", "Assembly"
]

def design_pattern():
    return ("Must use '{}' {} design pattern.".format(p, k)
            for k, v in design_patterns.items()
            for p in v)

# https://en.wikipedia.org/wiki/Software_design_pattern
design_patterns = {
    "creational": [
        "Lazy initialization", "Factory method",  "Dependency Injection",
        "Builder", "Abstract factory", "Multiton", "Object pool", "Prototype",
        "Singleton"
    ],
    "structural": [
        "Bridge", "Wrapper", "Composite", "Decorator", "Extension object",
        "Facade", "Flyweight", "Marker", "Module",
    ],
    "behavioral": [
        "Blackboard", "Chain of responsibility", "Command", "Interpreter",
        "Iterator", "Mediator", "Memento", "Null object", "Servant",
        "Specification", "State", "Strategy", "Template method", "Visitor"
    ],
    "concurency": [
        "Active Object", "Balking", "Binding properties", "Blockchain",
        "Compute kernel", "Double-checked locking", "Event-based asynchronous",
        "Guarded suspension", "Join", "Lock", "Thread pool", "Monitor object",
    ],
}

def taketh():
    return ("Cannot use any {}s.".format(p) for p in primitive_components)

# things we may take away.
primitive_components = [
    "string", "character", "int", "float", "number", "function", "loop", "boolean",
    "if statement", "conditional logic", "recursion", "hashmap", "array",
    "statment", "builtin", "alphabetic character", "hex character", "vowel"
]

natural_langs = [
    "English", "Spanish", "French", "Chinese", "Shakespearean English",
    "Backwards", "German", "Dutch", "Russian", "uppercase", "lowercase",
    "ascii codes seperated by underscores", "binary", "Olde English",
    "cockney rhyming slang"
]

text_types = [
    "function names", "varible names", "user defiened varible and function names",
    "comments", "text", "numbers"
]

def lang_switch():
    return ("Write all {} in {}".format(t, lang)
            for t in text_types
            for lang in natural_langs)

def numberwang():
    return ("Represent all numbers as {}.".format(n)
            for n in number_switches)

number_switches = [
    "hex", "binary", "octal", "roman numerals", "characters"
]


def write_again():
    return ("Write again {}.".format(w) for w in write_agains)

write_agains = [
    "in exactly half the amount of code",
    "in 10 minutes",
    "in 10 lines",
    "in double the amount of code",
    "with a 500 word introduction",
    "with a 1000 word introduction",
    "with greater respect for your peers",
    "with pen and paper",
    "with a type writer",
    "on your mobile phone",
    "on the oldest computer you can find",
    "in a way a 10 year old might understand",
    "then explain it someone who wouldnt have understood it originally"
]

def influence():
    return ("Should clearly be influenced by {}".format(w)
            for w in influences)

influences = [
    "hip-hop",
    "jazz",
    "classic rock",
    "heavy metal",
    "reggae",
    "punk rock",
    "country music",
    "electronic music",
    "soul",
    "funk",
    "spoken word",
    "post-modernism",
    "modernism",
    "classical archetecture",
    "baroque archetecture",
    "pop music",
    "Folk music",
    "Country music",
    "your favourite band",
    "your favourite music",
    "your favourite film",
    "your favourite tv show",
    "your favourite youtube channel",
    "facebook",
    "the internet"
]

def device():
    return ("redesign for {} device.".format(d)
            for d in devices)

devices = [
    "mobile", "micro-controller", "interet of things",
    "web", "audio", "visual", "text based", "robotic",
]

# -----------------------------------------------------------------------------

fun = [
    lang_switch, design_pattern, taketh, prog_lang, numberwang, write_again,
    device, influence,
]

cat = "\n".join
with open("obstructions.txt", "w") as fp:
    for f in fun:
        fp.write(cat(f()))
        fp.write("\n")