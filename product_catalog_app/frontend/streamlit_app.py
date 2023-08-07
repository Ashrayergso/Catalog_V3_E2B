```python
import streamlit as st
from backend import crud_operations, export_functionality, search_feature

def main():
    st.title("Product Catalog Application")

    menu = ["Home", "Add Product", "Update Product", "Delete Product", "Export Product List", "Search Product Alternatives"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Product List")
        products = crud_operations.read_product()
        st.dataframe(products)

    elif choice == "Add Product":
        st.subheader("Add New Product")
        product_name = st.text_input("Product Name")
        description = st.text_input("Description")
        product_number = st.text_input("Product Number")
        vendor_name = st.text_input("Vendor Name")
        cost = st.number_input("Cost")
        product_image = st.file_uploader("Product Image", type=["png", "jpg", "jpeg"])
        product_site = st.text_input("Product Site")

        if st.button("Add Product"):
            crud_operations.create_product(product_name, description, product_number, vendor_name, cost, product_image, product_site)

    elif choice == "Update Product":
        st.subheader("Update Product Information")
        product_list = crud_operations.read_product()
        product_names = product_list['product_name'].tolist()
        selected_product = st.selectbox("Select Product", product_names)

        product_info = crud_operations.read_product(selected_product)
        product_name = st.text_input("Product Name", product_info['product_name'])
        description = st.text_input("Description", product_info['description'])
        product_number = st.text_input("Product Number", product_info['product_number'])
        vendor_name = st.text_input("Vendor Name", product_info['vendor_name'])
        cost = st.number_input("Cost", product_info['cost'])
        product_image = st.file_uploader("Product Image", type=["png", "jpg", "jpeg"], value=product_info['product_image'])
        product_site = st.text_input("Product Site", product_info['product_site'])

        if st.button("Update Product"):
            crud_operations.update_product(selected_product, product_name, description, product_number, vendor_name, cost, product_image, product_site)

    elif choice == "Delete Product":
        st.subheader("Delete Product")
        product_list = crud_operations.read_product()
        product_names = product_list['product_name'].tolist()
        selected_product = st.selectbox("Select Product", product_names)

        if st.button("Delete Product"):
            crud_operations.delete_product(selected_product)

    elif choice == "Export Product List":
        st.subheader("Export Product List")
        if st.button("Export"):
            export_functionality.export_product_list()

    elif choice == "Search Product Alternatives":
        st.subheader("Search Product Alternatives")
        search_query = st.text_input("Enter Product Name")
        if st.button("Search"):
            results = search_feature.search_product_alternatives(search_query)
            st.dataframe(results)

if __name__ == "__main__":
    main()
```