from celery import shared_task

@shared_task
def update_product_stock(product_id):
    # Logic to check stock levels and notify the admin if low
    pass
