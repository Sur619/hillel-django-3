# import os
# from datetime import datetime
#
# from dotenv import load_dotenv
# from rest_framework.decorators import action
#
# from telegram.client import send_message
#
# load_dotenv()
#
# from django.db.models.signals import post_save, pre_save, post_delete, m2m_changed, post_init
# from django.dispatch import receiver
#
# from products.models import Order
# from products.tasks import order_send_telegram_message
#
#
# @receiver(post_save, sender=Order)
# def send_order_telegram_message(sender, instance: Order, created, **kwargs):
#     # if created:
#     #     chat_id = 980106016
#     #
#     #     order_products = instance.order_products.all()
#     #     text = f"new order {instance.uuid} created\n"
#     #     for order_product in order_products:
#     #         text += f"{order_product.product.title} - {order_product.quantity} - {order_product.price}\n"
#     #     send_message(chat_id, text)
#     if created:
#         order_send_telegram_message.apply_async((instance.uuid,), countdown=10)
#
#
# @receiver(pre_save, sender=Order)
# def assign_display_number(sender, instance, **kwargs):
#     instance.display_number = datetime.now().timestamp()
#
#
# @receiver(post_delete, sender=Order)
# def after_order_deleted(sender, instance, **kwargs):
#     print('order deleted')
#     chat_id = os.environ.get('TELEGRAM_BOT_CHAT_ID')
#     text = f"Order {instance.uuid} has been deleted."
#     send_message(chat_id, text)
#     print(action)
#
#
# @receiver(m2m_changed, sender=Order)
# def after_order_product_changed(sender, instance, **kwargs):
#     print('order product changed')
#     chat_id = os.environ.get('TELEGRAM_BOT_CHAT_ID')
#     text = f"Order {instance.uuid} has been changed."
#     send_message(chat_id, text)
#     print(action)
#
#
# @receiver(post_init, sender=Order)
# def after_order_initialized(sender, instance, **kwargs):
#     print('order initialization completed')
#     chat_id = os.environ.get('TELEGRAM_BOT_CHAT_ID')
#     text = f"Order {instance.uuid} has been initialized."
#     send_message(chat_id, text)
#     print(action)
