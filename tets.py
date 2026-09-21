except RequestException as error:
    now = datetime.datetime.now()
    error_data = {
        "timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
        "status_code": "N/A",
        "city": params.get("q"),
        "message": str(error)
    }
    write_error_log(error_data)