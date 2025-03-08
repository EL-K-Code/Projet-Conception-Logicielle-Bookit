// assets
// constant

// ==============================|| SAMPLE PAGE & DOCUMENTATION MENU ITEMS ||============================== //

const evenements = {
    id: 'events',
    title: 'Events',
    type: 'group',
    accessGroups:["event_admin"],
    children: [
        {
            id: 'bus',
            title: 'Add Bus Event',
            type: 'item',
            url: '/events/create/bus',
            breadcrumbs: false,
            accessGroups:["event_admin"]
        },
        {
            id: 'room',
            title: 'Add Room Event',
            type: 'item',
            url: '/events/create/room',
            breadcrumbs: false,
            accessGroups:["event_admin"]
        },
        {
            id: 'material',
            title: 'Add Material Event',
            type: 'item',
            url: '/events/create/material',
            breadcrumbs: false,
            accessGroups:["event_admin"]
        }
    ]
};

export default evenements;
