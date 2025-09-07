# PWA Push Notifications Module

This module integrates Odoo notifications with Firebase Cloud Messaging (FCM) to allow Progressive Web Apps (PWAs) on Android to receive push notifications.

## Features

- Firebase Cloud Messaging integration
- Device token management
- Background message handling via service worker
- Configuration through Odoo settings
- Bus system integration for automatic push notifications

## Installation

1. Place this module in your Odoo addons directory
2. Update your apps list
3. Install the "PWA Push Notifications (FCM)" module

## Configuration

1. Go to Settings > Technical > PWA Push Notifications
2. Configure your Firebase project settings:
   - Firebase API Key
   - Firebase Auth Domain
   - Firebase Project ID
   - Firebase Storage Bucket
   - Firebase Messaging Sender ID
   - Firebase App ID
   - Web Push VAPID Key
   - Service Account JSON Path (for server-side sending)

## Usage

1. Users will see an "Enable Notifications" button on the frontend
2. Clicking the button requests notification permission and registers the device
3. When Odoo sends bus notifications, they will automatically be forwarded as push notifications to registered devices

## Dependencies

- firebase-admin (Python package) - required for server-side push sending
- Firebase Web SDK - loaded from CDN in the frontend

## Technical Details

- **Controllers**: Handle Firebase configuration, token saving, and service worker
- **Models**: FCM device storage, configuration settings, bus integration
- **Frontend**: JavaScript client for Firebase integration
- **Security**: Proper access control for device tokens

## Files Structure

```
pwa_push_notifications/
├── __init__.py
├── __manifest__.py
├── controllers/
│   ├── __init__.py
│   └── main.py
├── models/
│   ├── __init__.py
│   ├── bus_inherit.py
│   ├── fcm_device.py
│   ├── res_config_settings.py
│   └── res_users.py
├── static/
│   └── src/
│       └── js/
│           └── push_client.js
├── views/
│   └── res_config_settings_views.xml
└── security/
    └── ir.model.access.csv
```