import logging

#cấu hình logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def check_service_status(service_name, status):
    logging.debug(f"Checking status: {service_name}")
    if status == "running":
        logging.info(f"Serice {service_name} is running.")
    else:
        logging.warning(f"service {service_name} is not running.")

#main function
if __name__ == "__main__":
    logging.info("Starting service status check...")
    check_service_status("Database", "running")
    check_service_status("Web Server", "stopped")
    logging.info("Service status check completed.")