// assets
import { IconBrandChrome, IconHelp } from '@tabler/icons-react';

// constant
const icons = {
    IconBrandChrome,
    IconHelp
};

// ==============================|| SAMPLE PAGE & DOCUMENTATION MENU ITEMS ||============================== //

const evenements = {
    id: 'events',
    title: 'Events',
    type: 'group',
    children: [
        {
            id: 'event-bus',
            title: 'Add Bus Event',
            type: 'item',
            url: '/events/create/bus',
            icon: icons.IconBrandChrome,
            breadcrumbs: false
        },
        {
            id: 'event-room',
            title: 'Add Room Event',
            type: 'item',
            url: '/events/create/room',
            icon: icons.IconHelp,
            breadcrumbs: false
        },
        {
            id: 'event-material',
            title: 'Add Material Event',
            type: 'item',
            url: '/events/create/material',
            icon: icons.IconHelp,
            breadcrumbs: false
        }
    ]
};

export default evenements;
