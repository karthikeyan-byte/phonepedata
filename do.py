def ma():
    st.title("phonepe pulse")
    options = st.sidebar.selectbox(
        "Select an option",
        ('Transactions', 'Users', )
    )
    if options == 'Transactions':
        opt=st.sidebar.selectbox(
            "Select an Year",
            ('2018', '2019', '2020','2021','2022','2023')
            )
        if opt == '2018':
            op=st.sidebar.selectbox(
                "Select a Quarter",
                ('Q1', 'Q2', 'Q3', 'Q4')
            )
            if op == 'Q1':
                tw(desired_year=2018, desired_quarter=1)
                map(df)
            if op == 'Q2':
                tw(desired_year=2018, desired_quarter=2)
            if op == 'Q3':
                tw(desired_year=2018, desired_quarter=3)
            if op == 'Q4':
                tw(desired_year=2018, desired_quarter=4)
        if opt == '2019':
            op=st.sidebar.selectbox(
                "Select a Quarter",
                ('Q1', 'Q2', 'Q3', 'Q4')
            )
            if op == 'Q1':
                tw(desired_year=2019, desired_quarter=1)
            if op == 'Q2':
                tw(desired_year=2019, desired_quarter=2)
            if op == 'Q3':
                tw(desired_year=2019, desired_quarter=3)
            if op == 'Q4':
                tw(desired_year=2019, desired_quarter=4)
        if opt == '2020':
            op=st.sidebar.selectbox(
                "Select a Quarter",
                ('Q1', 'Q2', 'Q3', 'Q4')
            )
            if op == 'Q1':
                tw(desired_year=2020, desired_quarter=1)
            if op == 'Q2':
                tw(desired_year=2020, desired_quarter=2)
            if op == 'Q3':
                tw(desired_year=2020, desired_quarter=3)
            if op == 'Q4':
                tw(desired_year=2020, desired_quarter=4)
        if opt == '2021':
            op=st.sidebar.selectbox(
                "Select a Quarter",
                ('Q1', 'Q2', 'Q3', 'Q4')
            )
            if op=='Q1':
                tw(desired_year=2021, desired_quarter=1)
            if op=='Q2':
                tw(desired_year=2021, desired_quarter=2)
            if op=='Q3':
                tw(desired_year=2021, desired_quarter=3)
            if op=='Q4':
                tw(desired_year=2021, desired_quarter=4)
        if opt=='2022':
            op=st.sidebar.selectbox(
                "Select a Quarter",
                ('Q1', 'Q2', 'Q3', 'Q4')
            )
            if op=='Q1':
                tw(desired_year=2022, desired_quarter=1)
            if op=='Q2':
                tw(desired_year=2022, desired_quarter=2)
            if op=='Q3':
                tw(desired_year=2022, desired_quarter=3)
            if op=='Q4':
                tw(desired_year=2022, desired_quarter=4)
        if opt=='2023':
            op=st.sidebar.selectbox(
                "Select a Quarter",
                ('Q1', 'Q2', 'Q3', 'Q4')
            )
            if op=='Q1':
                tw(desired_year=2023, desired_quarter=1)
            if op=='Q2':
                tw(desired_year=2023, desired_quarter=2)
            if op=='Q3':
                st.write(" DATA NOT AVAILABLE")
            if op=='Q4':
                st.write(" DATA NOT AVAILABLE")
    if options == 'Users':
        opt=st.sidebar.selectbox(
            "Select an Year",
            ('2018', '2019', '2020','2021','2022','2023')
            )
        if opt == '2018':
            op=st.sidebar.selectbox(
                "Select a Quarter",
                ('Q1', 'Q2', 'Q3', 'Q4')
            )
        if opt == '2019':
            op=st.sidebar.selectbox(
                "Select a Quarter",
                ('Q1', 'Q2', 'Q3', 'Q4')
            )
        if opt == '2020':
            op=st.sidebar.selectbox(
                "Select a Quarter",
                ('Q1', 'Q2', 'Q3', 'Q4')
            )
        if opt == '2021':
            op=st.sidebar.selectbox(
                "Select a Quarter",
                ('Q1', 'Q2', 'Q3', 'Q4')
            )
        if opt=='2022':
            op=st.sidebar.selectbox(
                "Select a Quarter",
                ('Q1', 'Q2', 'Q3', 'Q4')
            )
        if opt=='2023':
            op=st.sidebar.selectbox(
                "Select a Quarter",
                ('Q1', 'Q2', 'Q3', 'Q4')
            )
            
# Create a sidebar menu with options
menu_option = st.sidebar.selectbox(
    "Menu",
    ("Home", "Page 1")
)

# Define the content for each menu option
if menu_option == "Home":
    st.title("Home Page")
    st.write("Welcome to the Home Page!")
elif menu_option == "Page 1":
    ma()
 




