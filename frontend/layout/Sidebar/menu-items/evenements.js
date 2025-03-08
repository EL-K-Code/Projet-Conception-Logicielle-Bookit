// assets
// constant

// ==============================|| SAMPLE PAGE & DOCUMENTATION MENU ITEMS ||============================== //

const evenements = {
    id: 'events',
    title: 'Events',
    type: 'group',
    children: [
        {
            id: 'bus',
            title: 'Add Bus Event',
            type: 'item',
            url: '/events/create/bus',
            breadcrumbs: false,
        },
        {
            id: 'room',
            title: 'Add Room Event',
            type: 'item',
            url: '/events/create/room',
            breadcrumbs: false,
        },
        {
            id: 'material',
            title: 'Add Material Event',
            type: 'item',
            url: '/events/create/material',
            breadcrumbs: false,
        }
    ]
};

export default evenements;
