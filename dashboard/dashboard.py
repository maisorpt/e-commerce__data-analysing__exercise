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
#### 1. **Temuan Utama**  
   - **Jumlah Rating vs. Kategori Produk**: Beberapa kategori produk memiliki jumlah rating yang sangat dominan dibandingkan kategori lain. Hal ini menunjukkan tingkat popularitas atau tingkat adopsi yang berbeda antar kategori. Kategori dengan jumlah rating tertinggi cenderung menjadi kategori yang menarik perhatian pasar luas, sedangkan kategori dengan jumlah rating rendah kemungkinan memiliki audiens yang lebih spesifik atau ceruk.  
   - **Rating Rata-rata vs. Kategori Produk**: Rating rata-rata bervariasi secara signifikan antar kategori, dengan beberapa kategori menunjukkan konsistensi rating yang lebih tinggi. Kategori tertentu secara konsisten menerima rating tinggi, mengindikasikan kepuasan pelanggan yang lebih baik terhadap produk di kategori tersebut. Sebaliknya, kategori dengan rating rata-rata rendah menunjukkan adanya potensi masalah pada produk atau ekspektasi pelanggan yang tidak terpenuhi.  
   

#### 2. **Interpretasi**  
   - **Kategori dengan Jumlah Rating Tinggi**: Jumlah rating yang tinggi seringkali mencerminkan pasar yang besar dan kompetitif. Hal ini juga bisa menunjukkan kesadaran merek yang kuat, strategi distribusi yang efektif, atau produk yang sering dibeli dalam jumlah besar.  
   - **Kategori dengan Rating Rata-rata Tinggi**: Kategori dengan rating rata-rata tinggi mencerminkan produk yang memenuhi ekspektasi pelanggan atau bahkan melampauinya. Ini dapat disebabkan oleh kualitas produk yang superior, pengalaman pengguna yang memuaskan, atau persepsi merek yang positif.  
   - **Kategori dengan Rating Rata-rata Rendah**: Rating rendah dapat mengindikasikan kelemahan pada kualitas produk, layanan, atau ketidaksesuaian antara produk dan kebutuhan pelanggan. Ini juga dapat mengindikasikan ulasan negatif akibat pengalaman buruk atau ekspektasi yang tidak sesuai dengan realitas.  
   - **Hubungan Rating dan Kategori**: Adanya variasi antara jumlah rating dan rating rata-rata mengindikasikan bahwa kategori populer tidak selalu berkorelasi dengan kepuasan pelanggan. Beberapa kategori mungkin memiliki volume tinggi tetapi rating rendah, mencerminkan potensi masalah kepuasan meskipun produknya banyak digunakan.  
   

#### 3. **Rekomendasi**  
   - **Untuk Kategori dengan Jumlah Rating Tinggi dan Rating Rata-rata Rendah**:  
     a. Fokus pada analisis mendalam terkait ulasan negatif untuk memahami aspek-aspek yang perlu diperbaiki, seperti kualitas produk, pelayanan, atau ekspektasi yang tidak terpenuhi.  
     b. Lakukan survei pelanggan untuk mengidentifikasi kebutuhan dan ekspektasi yang lebih spesifik.  
     c. Perbaiki komunikasi pemasaran agar tidak menjanjikan hal yang berlebihan dibandingkan realitas produk.  
   - **Untuk Kategori dengan Rating Rata-rata Tinggi**:  
     a. Manfaatkan keunggulan ini sebagai daya tarik pemasaran, seperti menonjolkan testimoni pelanggan atau penghargaan yang relevan.  
     b. Pertimbangkan ekspansi ke segmen pasar lain dengan strategi yang serupa untuk meningkatkan pangsa pasar.  
     c. Evaluasi apakah atribut yang membuat kategori ini unggul dapat diterapkan ke kategori lain.  
   - **Untuk Kategori dengan Jumlah Rating Rendah**:  
     a. Lakukan promosi atau kampanye pemasaran untuk meningkatkan visibilitas kategori tersebut di pasar.  
     b. Evaluasi apakah produk di kategori ini sesuai dengan kebutuhan pasar saat ini. Jika tidak, pertimbangkan untuk melakukan inovasi atau reposisi produk.  
   - **Secara Umum**:  
     a. Perkuat strategi pengumpulan ulasan dengan mendorong pelanggan memberikan feedback secara sukarela melalui insentif atau program loyalitas.  
     b. Gunakan data ulasan untuk membuat keputusan berbasis data, seperti memperbaiki fitur produk atau mengubah strategi harga.  
     c. Lakukan benchmarking dengan kompetitor untuk memahami keunggulan dan kelemahan relatif di setiap kategori.  

---
                     
### Q2: Apa faktor-faktor yang paling berpengaruh terhadap total penjualan produk?
   #### **Kesimpulan Berdasarkan Data**  

1. **Jumlah Ulasan Sebagai Faktor Utama**  
   - **Temuan:** Korelasi sangat tinggi antara jumlah ulasan (*review_count*) dan total penjualan (*sold_count*) (**0.9999**) menunjukkan bahwa produk dengan lebih banyak ulasan cenderung terjual lebih banyak.  
   - **Mengapa Penting:** Jumlah ulasan mencerminkan tingkat keterlibatan pelanggan, menciptakan kepercayaan bagi calon pembeli. Produk dengan banyak ulasan lebih terlihat populer dan memiliki bukti sosial yang kuat.  
   - **Rekomendasi:** Fokus pada strategi untuk mendorong lebih banyak ulasan dari pelanggan, seperti memberikan insentif untuk ulasan atau menggunakan pengingat otomatis pasca-pembelian.

2. **Harga Memiliki Pengaruh Negatif, Tetapi Tidak Signifikan**  
   - **Temuan:** Korelasi negatif yang sangat lemah antara harga rata-rata produk (*avg_item_price*) dan total penjualan (**-0.0661**) menunjukkan bahwa harga tidak memainkan peran besar dalam memengaruhi penjualan secara keseluruhan.  
   - **Mengapa Penting:** Pembeli mungkin lebih mementingkan nilai daripada harga mutlak, terutama jika produk terlihat populer (banyak ulasan) atau memiliki kualitas yang tinggi.  
   - **Rekomendasi:** Jangan hanya berfokus pada menurunkan harga untuk meningkatkan penjualan. Sebaliknya, berikan nilai tambah seperti deskripsi produk yang lebih menarik, diskon bundling, atau peningkatan layanan pelanggan.

3. **Skor Rata-Rata Ulasan Hampir Tidak Berpengaruh**  
   - **Temuan:** Korelasi lemah antara skor rata-rata ulasan (*average_review_score*) dan total penjualan (**0.0143**) menunjukkan bahwa jumlah ulasan lebih penting daripada skor rata-rata ulasan.  
   - **Mengapa Penting:** Ini mungkin disebabkan karena pembeli lebih dipengaruhi oleh kuantitas ulasan dibandingkan kualitasnya, terutama jika skor tidak terlalu buruk.  
   - **Rekomendasi:** Fokus pada menjaga skor ulasan dalam kategori “baik” (contoh: di atas 4 dari 5). Jangan terlalu khawatir dengan ulasan yang sedikit negatif, tetapi tetap tanggapi ulasan buruk dengan cepat untuk menjaga reputasi.


#### **Mengapa Hasil Ini Terjadi?**  
- **Peran Bukti Sosial:** Banyaknya ulasan menciptakan persepsi positif bahwa produk tersebut banyak digunakan oleh orang lain, sehingga meningkatkan kepercayaan calon pembeli.  
- **Persepsi Nilai Lebih Penting daripada Harga:** Pembeli tidak terlalu sensitif terhadap harga jika mereka merasa produk memberikan nilai yang cukup.  
- **Kualitas Ulasan Tidak Terlalu Dominan:** Selama skor ulasan tidak terlalu buruk, pembeli mungkin lebih fokus pada kuantitas ulasan karena lebih meyakinkan.


#### **Tindakan Strategis yang Direkomendasikan:**  
1. **Mendorong Lebih Banyak Ulasan:**  
   - Terapkan program insentif, seperti diskon untuk ulasan, atau kampanye email untuk mengingatkan pembeli memberikan ulasan.  
   - Optimalkan pengalaman pembelian untuk meningkatkan kepuasan pelanggan, yang secara alami memotivasi mereka memberikan ulasan positif.

2. **Menambah Nilai Tanpa Fokus Utama pada Harga:**  
   - Tawarkan bundling produk, diskon terbatas waktu, atau manfaat lain yang membuat pembeli merasa mendapatkan lebih banyak.  
   - Berikan fokus pada pemasaran visual dan *copywriting* yang menunjukkan manfaat produk.

3. **Jaga Kualitas Produk dan Tanggapi Ulasan Buruk:**  
   - Pastikan produk memiliki kualitas memadai sehingga skor ulasan tidak jatuh terlalu rendah.  
   - Gunakan ulasan negatif sebagai peluang untuk memperbaiki layanan dan membangun kepercayaan dengan merespons secara profesional.
             
### Note:
- Data di atas memberikan wawasan yang berguna untuk memanfaatkan faktor-faktor seperti harga, ulasan, dan kategori dalam strategi penjualan dan pemasaran.
    """)
    st.write("📈 **Further Exploration**: Consider exploring correlations between other variables and sales for a deeper insight.")
