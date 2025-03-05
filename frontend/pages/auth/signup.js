"use client";

import Auth from "@/components/authentication/Auth";


// ================================|| LOGIN ||================================ //

export default function Login() {

    return (
        <Auth route="/api/auth/signup/" method="signup" />
    );
};

