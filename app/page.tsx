import Image from 'next/image'
import Link from 'next/link'

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 w-full max-w-5xl items-center justify-between font-mono text-sm lg:flex">
        <h1 className="text-2xl font-semibold">My Blog</h1>
        <nav className="flex justify-between mt-6">
          <a href="/" className="text-gray-800 hover:text-gray-900">Home</a>
          <a href="/about" className="text-gray-800 hover:text-gray-900">About</a>
          <a href="/posts" className="text-gray-800 hover:text-gray-900">Posts</a>
        </nav>
      </div>

      <div className="flex flex-col justify-center mt-8">
        <div className="flex flex-col">
          <h2 className="text-xl font-semibold">Posts</h2>
          <div className="posts">
            No posts yet
          </div>
        </div>

        <div className="mt-12">
          <h2 className="text-xl font-semibold">Add a Post</h2>
          <form action="/posts" method="post">
            <input type="text" name="title" placeholder="Title" />
            <input type="text" name="content" placeholder="Content" />
            <button type="submit">Add Post</button>
          </form>
        </div>
      </div>
    </main>
  )
}