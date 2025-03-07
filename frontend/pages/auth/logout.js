import { useRouter } from "next/navigation";

export default function LogOut(){
    const router = useRouter();
    localStorage.clear()
    return router.push("/auth/login");

}