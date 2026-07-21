import streamlit as st

from backend import *

st.set_page_config(

    page_title="Mobile Repository",

    page_icon="📱",

    layout="wide"

)

st.title("📱 Mobile Repository")

choice = st.sidebar.selectbox(

    "Choose Operation",

    [

        "Add Mobile",

        "View Mobiles",

        "Update Mobile",

        "Delete Mobile",

        "Search Mobile",

        "Sort by Price",

        "AI Assistant"

    ]

)

# -------------------- ADD --------------------

if choice == "Add Mobile":

    st.header("➕ Add Mobile")

    name = st.text_input("Mobile Name")

    brand = st.text_input("Brand")

    price = st.number_input(

        "Price",

        min_value=0,

        step=100

    )

    if st.button("Add"):

        add_mobile(name, brand, price)

        st.success("Mobile Added Successfully")


# -------------------- VIEW --------------------

elif choice == "View Mobiles":

    st.header("📄 Mobile Inventory")

    data = view_mobiles()

    if data:

        st.dataframe(data, use_container_width=True)

    else:

        st.info("Inventory is empty.")


# -------------------- UPDATE --------------------

elif choice == "Update Mobile":

    st.header("✏ Update Mobile")

    old_name = st.text_input("Existing Mobile Name")

    new_name = st.text_input("New Mobile Name")

    brand = st.text_input("New Brand")

    price = st.number_input(
        "New Price",
        min_value=0,
        step=100
    )

    if st.button("Update"):

        if update_mobile(old_name, new_name, brand, price):

            st.success("Mobile Updated Successfully")

        else:

            st.error("Mobile Not Found")

# -------------------- DELETE --------------------

elif choice == "Delete Mobile":

    st.header("🗑 Delete Mobile")

    name = st.text_input("Mobile Name")

    if st.button("Delete"):

        if delete_mobile(name):

            st.success("Deleted Successfully")

        else:

            st.error("Mobile Not Found")


# -------------------- SEARCH --------------------

elif choice == "Search Mobile":

    st.header("🔍 Search")

    keyword = st.text_input("Keyword")

    if st.button("Search"):

        result = search_mobile(keyword)

        if result:

            st.dataframe(result, use_container_width=True)

        else:

            st.warning("No Mobile Found")


# -------------------- SORT --------------------

elif choice == "Sort by Price":

    st.header("💰 Mobiles Sorted by Price")

    data = sort_price()

    if data:

        st.dataframe(data, use_container_width=True)

    else:

        st.info("Inventory is empty.")


# -------------------- AI --------------------

elif choice == "AI Assistant":

    st.header("🤖 Gemini Assistant")

    question = st.text_area("Ask anything about mobiles")

    if st.button("Ask AI"):

        with st.spinner("Thinking..."):

            answer = ask_ai(question)

        st.write(answer)