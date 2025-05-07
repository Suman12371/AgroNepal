from .models import Cart, Notification, WalletWithdrawal, Order, Product, DealChatMessage

def cart_processor(request):
    """Context processor to add cart count and items to all templates"""
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        cart_count = cart_items.count()
        cart_total = sum(item.total_price() for item in cart_items)
        return {
            'cart_items': cart_items,
            'cart_count': cart_count,
            'cart_total': cart_total
        }
    return {
        'cart_items': [],
        'cart_count': 0,
        'cart_total': 0
    }

def notification_processor(request):
    """Context processor to add notification count to all templates"""
    if request.user.is_authenticated:
        unread_notifications = Notification.objects.filter(user=request.user, is_read=False).count()
        # Add pending withdrawals count for admin/co-admin users
        pending_withdrawals = 0
        if request.user.is_staff or hasattr(request.user, 'coadmin_profile'):
            pending_withdrawals = WalletWithdrawal.objects.filter(status='pending').count()
        
        return {
            'unread_notifications': unread_notifications,
            'pending_withdrawals': pending_withdrawals,
        }
    return {
        'unread_notifications': 0,
        'pending_withdrawals': 0,
    }

def count_notifications(request):
    """Context processor to count notifications for admin and co-admin dashboards"""
    context = {}
    
    if request.user.is_authenticated:
        # Count pending orders
        pending_orders = Order.objects.filter(status='pending').count()
        context['pending_orders'] = pending_orders
        
        # Count pending withdrawals
        pending_withdrawals = WalletWithdrawal.objects.filter(status='pending').count()
        context['pending_withdrawals'] = pending_withdrawals
        
        # Count processed withdrawals (for admin history page)
        processed_withdrawals = WalletWithdrawal.objects.filter(status__in=['approved', 'rejected']).count()
        context['processed_withdrawals'] = processed_withdrawals
        
        # Count low stock products
        low_stock_count = Product.objects.filter(stock__lt=10, is_available=True).count()
        context['low_stock_count'] = low_stock_count
        
        # Count unread messages
        if hasattr(request.user, 'coadmin_profile'):
            unread_deal_messages = DealChatMessage.objects.filter(
                receiver=request.user,
                is_read=False
            ).count()
            context['unread_deal_messages'] = unread_deal_messages
    
    return context 