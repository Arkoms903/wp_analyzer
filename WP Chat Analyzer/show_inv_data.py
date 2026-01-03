def show_individual_data(selected_user , df):
    if selected_user == 'overall':
        return df
    else:
        return df[df['user'] == selected_user]