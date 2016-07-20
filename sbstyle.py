# coding: utf-8

"""
 LaTeX2WPSC - the program that converts a LaTeX 
 document written in Serbian Cyrillic into a format  that is ready to be 
 copied and pasted  into WordPress
 
 Copyright 2009 by Luca Trevisan, Siniša Bubonja
 
 Additional contributors: Radu Grigore
 
 LaTeX2WPSC version 1.0.0

 This file is part of LaTeX2WPSC, a program that derives from previous 
 work on LaTeX2WP version 0.6.2 by Luca Trevisan and his contributor 
 Radu Grigore. Program is modified on the 9st August, 2013. For detailed 
 information read from a changelog.txt file.

 You are free to redistribute and/or modify LaTeX2WPSC under the
 terms of the GNU General Public License (GPL), version 3
 or (at your option) any later version.

 I hope you will find LaTeX2WPSC useful, but be advised that
 it comes WITHOUT ANY WARRANTY; without even the implied warranty
 of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GPL for more details.

 You should have received a copy of the GNU General Public
 License along with LaTeX2WPSC.  If you can't find it,
 see <http://www.gnu.org/licenses/>.
"""

# Lines starting with #, like this one, are comments

# color of LaTeX formulas
textcolor = "000000"

# colors that can be used in the text
colors = { "red" : "ff0000" , "green" : "00ff00" , "blue" : "0000ff" }
# list of colors defined above
colorchoice = ["red","green","blue"]

# counters for theorem-like environments
# assign any counter to any environment. Make sure that
# maxcounter is an upper bound to the any counter being used

T = { "axiom" : 0, "definition" : 1, "theorem" : 2, "proposition" : 3,
			"lemma" : 4, "corollary" : 5, "conjecture" : 6, "example" : 7,
			"exercise" : 8, "problem" : 9, "task" : 10 , "remark" : 11 }

# list of theorem-like environments
ThmEnvs = ["axiom","definition","theorem","proposition","lemma","corollary",
			"conjecture","example","exercise","problem","task","remark"]

# the way \begin{theorem}, \begin{lemma} etc are translated in HTML
# the string _ThmType_ stands for the type of theorem
# the string _ThmNumb_ is the theorem number

beginthm = "\n<blockquote style='border:solid black 1px; padding-left:10px; padding-right:10px; padding-bottom:10px; padding-top:10px;'><b>_ThmType_ _ThmNumb_.</b><em><i>"

# translation of \begin{theorem}[...]. The string
# _ThmName_ stands for the content betwee the
# square brackets
beginnamedthm = "\n<blockquote style='border:solid black 1px; padding-left:10px; padding-right:10px; padding-bottom:10px; padding-top:10px;'><b>_ThmType_ _ThmNumb_. (_ThmName_)</b><em><i>"
	
	#translation of \end{theorem}, \end{lemma}, etc.
endthm = "</i></em></blockquote>\n<p>\n"

beginproof = "<b>ДОКАЗ:</b>"
endproof = "$latex \Box&fg=000000$\n\n"

beginsolution = "<b>РЈЕШЕЊЕ:</b>"
endsolution = "$latex \Box&fg=000000$\n\n"

begininstruction = "<b>УПУТСТВО:</b>"
endinstruction = "$latex \\triangle&fg=000000$\n\n"

section = "\n<p align=center><strong> &mdash;  _SecNumb_. _SecName_  &mdash; </strong></p>\n\n"
sectionstar = "\n<p align=center><strong> &mdash; _SecName_  &mdash; </strong></p>\n\n"
subsection = "\n<p align=center><strong> &mdash;  _SecNumb_._SubSecNumb_. _SecName_  &mdash; </strong></p>\n\n"
subsectionstar = "\n<p align=center><strong> &mdash;   _SecName_  &mdash;</strong></p>\n\n"


# Font styles. Feel free to add others. The key *must* contain
# an open curly bracket. The value is the namem of a HTML tag.
fontstyle = {
  r'{\em ' : 'em',
  r'{\bf ' : 'b',
  r'{\it ' : 'i',
  r'{\sl ' : 'i',
  r'\textit{' : 'i',
  r'\textsl{' : 'i',
  r'\emph{' : 'em',
  r'\textbf{' : 'b',
}

# Macro definitions
# It is a sequence of pairs [string1,string2], and
# latex2wp will replace each occurrence of string1 with an
# occurrence of string2. The substitutions are performed
# in the same order as the pairs appear below.
# Feel free to add your own.
# Note that you have to write \\ instead of \
# and \" instead of "

M = [     ["\\to","\\rightarrow"] ,
          ["\\B","\\{ 0,1 \\}" ],
          ["\\E","\mathop{\\mathbb E}"],
          ["\\P","\mathop{\\mathbb P}"],
          ["\\N","{\\mathbb N}"],
          ["\\Z","{\\mathbb Z}"],
          ["\\Co","{\\mathbb C}"],
          ["\\R","{\\mathbb R}"],
          ["\\Q","{\\mathbb Q}"],
          ["\\xor","\\oplus"],
          ["\\eps","\\epsilon"]
    ]

