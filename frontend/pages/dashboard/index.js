"use client";

import EarningCard from "@/components/dashboard/EarningCard";
import { Grid } from "@mui/material";
import { useEffect, useState } from "react";

function Dashboard() {
    const [isLoading, setLoading] = useState(true);

    useEffect(() => {
        setLoading(false);
    }, []);

    return (
        <Grid container spacing={2}>
            <Grid item xs={12} sm={6} md={4} lg={3}>
                <EarningCard isLoading={isLoading} />
            </Grid>
        </Grid>
    );
}

export default Dashboard;
