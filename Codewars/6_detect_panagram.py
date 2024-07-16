def is_pangram(st):
    return 'abcdefghijklmnopqrstuvwxyz' in ''.join(sorted(set(st.casefold())))