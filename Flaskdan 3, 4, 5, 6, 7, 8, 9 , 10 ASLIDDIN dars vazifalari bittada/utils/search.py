def highlight_words(text,term,start_teg,end_teg):
  text=text.replace(term, start_teg + term + end_teg)

  return text