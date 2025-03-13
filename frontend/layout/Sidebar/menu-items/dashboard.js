// assets
import { IconDashboard } from '@tabler/icons-react';

// constant
const icons = {
    IconDashboard
};

// ==============================|| DASHBOARD MENU ITEMS ||============================== //

const dashboard = {
    id: 'home',
    title: 'Home',
    type: 'group',
    accessGroups:["anonymous", "consumer", "event_admin", "admin"],
    children: [
        {
            id: 'dashboard',
            title: 'Dashboard',
            type: 'item',
            url: '/',
            icon: icons.IconDashboard,
            breadcrumbs: false,
            accessGroups:["anonymous", "consumer", "event_admin", "admin"]
        }
    ]
};

export default dashboard;
