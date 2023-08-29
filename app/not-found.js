import Link from 'next/link'
 
export default function NotFound() {
  return (
    <div>
      <h2>Not Found</h2>
      <p>Sorry couldn't find what you were looking for</p>
      <Link href="/">Retreat?</Link>
    </div>
  )
}