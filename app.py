
import streamlit as st 
import string 
import random 
from ultimate_wordlist import animals_list,adjectives_list,negative_wordlist,positive_wordlist

# Fxn
def custom_filter(mylist,start_char):
	results = [i for i in mylist if i.startswith(start_char)]
	return results


# # Fxn with typing
# def custom_filter(mylist: list,start_char:str) -> list:
# 	results = [i for i in mylist if i.startswith(start_char)]
# 	return results





def main():
	st.title("Ambivalent & Ubuntu Names Generator App")
	st.subheader("Streamlit Projects")

	menu = ["Home","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		# layout
		col1 = st.columns(1)

		with col1:
			st.info("Ubuntu Names Generator")
			alphabeth_type = st.selectbox("Startwith",list(string.ascii_uppercase))
			if st.button("Generate Ubuntu Name"):
				custom_animals_list = custom_filter(animals_list,alphabeth_type.lower())
				custom_adjectives_list = custom_filter(adjectives_list,alphabeth_type.lower())
				results =  random.choice(custom_adjectives_list) + ' ' + random.choice(custom_animals_list)
				st.write(results)

				# Copy
				st.code(results)

		with col2:
			st.success("TBD")




	else:
		st.subheader("About")


if __name__ == '__main__':
	main()


