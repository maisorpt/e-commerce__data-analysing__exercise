import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Load the data
bycategory_combined_df = pd.read_csv('bycategory_combined_data.csv')
byproduct_combined_df = pd.read_csv('byproduct_combined_data.csv')

# Set up the Streamlit page configuration
st.set_page_config(page_title="Product Sales and Reviews Dashboard", layout="wide")

# Sidebar with selection options
st.sidebar.title("Navigation")
st.sidebar.markdown("Select the visualizations you want to explore:")

# Page Title
st.title("📊 Product Sales and Reviews Dashboard")

# Option to choose which visualization to show
page = st.sidebar.selectbox("Choose a page", ["Overview", "Review vs Sales", "Sales by Category", "Price and Sales Analysis", "Conclusion"])

# Overview Page
# Overview Page
if page == "Overview":
    st.header("📝 Overview of the Data")
    
    # Pilih dataset untuk ditampilkan
    dataset_choice = st.selectbox("Pilih dataset untuk ditampilkan", ["bycategory_combined_df", "byproduct_combined_df"])

    plt.figure(figsize=(4, 6))
    correlation_matrix = bycategory_combined_df[["total_sales", "avg_item_price", "review_count", "average_review_score"]].corr()
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".1f", square=True, 
                annot_kws={"fontsize": 6}, cbar_kws={"shrink": 0.3, "label": "Correlation Value"})
    heatmap.collections[0].colorbar.set_label("Correlation Value", fontsize=6)
    heatmap.collections[0].colorbar.ax.tick_params(labelsize=6)
    plt.xticks(rotation=45, fontsize=6)  # Adjust x-axis tick label font size
    plt.yticks(fontsize=6)  # Adjust y-axis tick label font size
    plt.tight_layout()
    
    if dataset_choice == "bycategory_combined_df":
        st.write(bycategory_combined_df.head())
        st.write("### Summary Statistics:")
        st.write(bycategory_combined_df.describe())
        st.write("### Correlation Between Sales and Other Factors:")
        st.pyplot(plt)
    else:
        st.write(byproduct_combined_df.head())
        st.write("### Summary Statistics:")
        st.write(byproduct_combined_df.describe())
        st.write("### Correlation Between Sales and Other Factors:")
        st.pyplot(plt)
    


# Review vs Sales Page
if page == "Review vs Sales":
    st.header("📈 Review Count vs Average Review Score by Category")
    
    plt.figure(figsize=(12, 8))

    scatter = sns.scatterplot(
        x="review_count",
        y="average_review_score",
        size="sold_count",
        hue="review_count",
        data=bycategory_combined_df,
        sizes=(50, 500),
        palette="coolwarm"
    )

    # Add reference lines
    plt.axvline(2000, color='gray', linestyle='--', linewidth=1.5, label='Review Count = 2000')
    plt.axhline(
        y=bycategory_combined_df['average_review_score'].mean(),
        color='red',
        linestyle='--',
        linewidth=1.5,
        label='Average Rating'
    )

    # Customize plot elements
    plt.xlabel("Number of Reviews")
    plt.ylabel("Average Review Score")

    # Truncate legend if there are many categories
    handles, labels = scatter.get_legend_handles_labels()
    plt.legend(
        handles=handles[:10] if len(handles) > 10 else handles,
        labels=labels[:10] if len(labels) > 10 else labels,
        title="Legend",
        loc="upper right",
        bbox_to_anchor=(1.25, 1)
    )

    # Display the plot in Streamlit
    st.pyplot(plt)

# Sales by Category Page
if page == "Sales by Category":

    dataset_choice = st.selectbox("Top Categories Based on", ["item_sold_by_category", "sales_by_category"])

    if dataset_choice == "item_sold_by_category":
        st.header("📊 Top Product Categories by Item Sold")

        # Show top categories by total sales
        top_sold_categories = bycategory_combined_df.sort_values(by='sold_count', ascending=False).head(10)

         # Create the bar plot
        plt.figure(figsize=(10, 6))
        sns.barplot(
            x="sold_count", y="product_category_name", data=top_sold_categories,
            palette="Greens_r"
        )
        
        # Set the title and labels
        plt.title("Top 10 Product Categories by Total Item Sold", fontsize=14)
        plt.xlabel("Total Items Sold")  # Label with 'millions' for better understanding
        plt.ylabel(None)
        
        # Show the plot
        st.pyplot(plt)
    else:
        st.header("📊 Top Product Categories by Total Sales")
    
        # Show top categories by total sales
        top_sales_categories = bycategory_combined_df.sort_values(by='total_sales', ascending=False).head(10)
        
        # Create the bar plot
        plt.figure(figsize=(10, 6))
        sns.barplot(
            x="total_sales", y="product_category_name", data=top_sales_categories,
            palette="Greens_r"
        )
        
        # Set the title and labels
        plt.title("Top 10 Product Categories by Total Sales", fontsize=14)
        plt.xlabel("Total Sales (in millions)")  # Label with 'millions' for better understanding
        plt.ylabel(None)
        
        # Format the x-axis to display in millions (optional adjustment)
        plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'${x/1e6:.2f}M'))  # Format as millions
        
        # Show the plot
        st.pyplot(plt)


# Price and Sales Analysis Page
if page == "Price and Sales Analysis":
    st.header("💸 Price vs Total Items Sold")
    
    # Pilih dataset untuk analisis harga dan penjualan
    dataset_choice = st.selectbox("Pilih dataset untuk analisis", ["bycategory_combined_df", "byproduct_combined_df"])
    
    if dataset_choice == "bycategory_combined_df":
        # Convert total_sales to numeric, and handle non-numeric values
        bycategory_combined_df['total_sales'] = pd.to_numeric(bycategory_combined_df['total_sales'], errors='coerce')

        # Scatter plot Price vs Total Sales (in millions)
        plt.figure(figsize=(12, 8))
        scatter = sns.scatterplot(
            x="sold_count", y="avg_item_price",  # Total sales in millions
            size="review_count", hue="average_review_score",
            data=bycategory_combined_df, sizes=(50, 300), palette="coolwarm"
        )
        

        # Add a title and labels
        plt.title("Price vs Total Items Sold by Category", fontsize=14)
        plt.xlabel("Item Sold")
        plt.ylabel("Average Item Price")

        # Show legend and plot
        handles, labels = scatter.get_legend_handles_labels()
        plt.legend(
            handles=handles[:10] if len(handles) > 10 else handles,
            labels=labels[:10] if len(labels) > 10 else labels,
            title="Legend",
            loc="upper right",
            bbox_to_anchor=(1.25, 1)
        )

        st.pyplot(plt)


    else:
        # Convert total_sales to numeric for byproduct_combined_df
        byproduct_combined_df['total_sales'] = pd.to_numeric(byproduct_combined_df['total_sales'], errors='coerce')

        # Scatter plot Price vs Total Sales for byproduct_combined_df
        plt.figure(figsize=(12, 8))
        scatter = sns.scatterplot(
            x="sold_count", y="item_price", 
            size="review_count", hue="average_review_score",
            data=byproduct_combined_df, sizes=(50, 300), palette="coolwarm"
        )
        plt.title("Price vs TItems Sold by Product", fontsize=14)
        plt.xlabel("Total Items Sold")
        plt.ylabel("Item Price")
        
        # Show legend and plot
        handles, labels = scatter.get_legend_handles_labels()
        plt.legend(
            handles=handles[:10] if len(handles) > 10 else handles,
            labels=labels[:10] if len(labels) > 10 else labels,
            title="Legend",
            loc="upper right",
            bbox_to_anchor=(1.25, 1)
        )
        st.pyplot(plt)


# Conclusion Page
if page == "Conclusion":
    st.header("📚 Conclusion")
    st.write("""
    ### Q1: Bagaimana hubungan antara rating produk dan kategori produk dalam hal jumlah ulasan dan rating rata-rata, dan apakah kategori produk tertentu memiliki rating lebih tinggi daripada yang lain?
    Hubungan antara rating produk dan kategori produk menunjukkan bahwa kategori dengan ulasan lebih dari 2000 memiliki rating yang lebih konsisten, sementara kategori dengan ulasan kurang dari 2000 cenderung memiliki rating yang lebih bervariasi. Beberapa kategori produk memiliki rating lebih tinggi daripada yang lain, tergantung pada jumlah ulasan yang diterima.

    ### Q2: Apa faktor-faktor yang paling berpengaruh terhadap total penjualan produk?
   Berdasarkan data yang diperoleh, terdapat korelasi yang lemah antar variabel yang dianalisis. Meskipun terdapat hubungan antara jumlah barang yang terjual `sold_count`, harga rata-rata barang `avg_item_price`, jumlah ulasan `review_count`, dan skor ulasan rata-rata `average_review_score`, nilai koefisien korelasinya menunjukkan hubungan yang cukup rendah. Sebagai contoh, hubungan antara jumlah barang yang terjual dan harga rata-rata barang memiliki koefisien negatif sebesar -0.066, yang menunjukkan adanya sedikit penurunan harga dengan peningkatan jumlah barang terjual. Demikian pula, hubungan antara harga rata-rata barang dan jumlah ulasan juga menunjukkan korelasi negatif kecil. Secara keseluruhan, analisis ini menunjukkan bahwa faktor-faktor ini tidak saling berpengaruh kuat satu sama lain dalam dataset yang ada.
             
    #### Note:
    - Data di atas memberikan wawasan yang berguna untuk memanfaatkan faktor-faktor seperti harga, ulasan, dan kategori dalam strategi penjualan dan pemasaran.
    """)
    st.write("📈 **Further Exploration**: Consider exploring correlations between other variables and sales for a deeper insight.")
