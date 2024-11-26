import parser as arg_parse
import process_df as *
import process_hist as *

if __name__ == "__main__":
    csv_path = arg_parse()
    try:
        data_frame = make_dataframe(csv_path)
        add_columns(data_frame)
        print(data_frame, "\n\n")

        stat = get_stat_info(data_frame)
        print(stat, "\n\n")

        sorted = sorted_df(data_frame, 1000, 1000)
        print(sorted, "\n\n")

        final_data_frame = add_area_column(data_frame)
        print(final_data_frame, "\n\n")

        make_hist(final_data_frame)
    except Exception as e:
        print(f"Program has failed: {e}")
