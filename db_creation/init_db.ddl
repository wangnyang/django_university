create extension "uuid-ossp";

create table if not exists faculty (
    id uuid primary key default uuid_generate_v4(),
    title text not null,
    description text
);

create table if not exists subject (
    id uuid primary key default uuid_generate_v4(),
    title text not null
);

create table if not exists teacher (
    id uuid primary key default uuid_generate_v4(),
    full_name text not null
);

create table if not exists class (
    id uuid primary key default uuid_generate_v4(),
    title text not null,
    faculty_id uuid REFERENCES faculty
);

create table if not exists student (
    id uuid primary key default uuid_generate_v4(),
    full_name text not null,
    class_id uuid REFERENCES class,
    created timestamp with time zone default current_timestamp
);

create table if not exists lesson (
    id uuid primary key default uuid_generate_v4(),
    day date not null,
    precise_time time not null,
    subject_id uuid not null REFERENCES subject,
    teacher_id uuid not null REFERENCES teacher
);

create table if not exists mark (
    id uuid primary key default uuid_generate_v4(),
    mark int,
    presence text,
    student_id uuid not null REFERENCES student,
    lesson_id uuid not null REFERENCES lesson,
    created timestamp with time zone default current_timestamp,
    modified timestamp with time zone default current_timestamp
);

create table if not exists subject_to_class (
    id uuid primary key default uuid_generate_v4(),
    subject_id uuid not null REFERENCES subject,
    class_id uuid not null REFERENCES class
);

CREATE UNIQUE INDEX subject_to_class_idx ON subject_to_class (subject_id, class_id);

create table if not exists subject_to_teacher (
    id uuid primary key default uuid_generate_v4(),
    subject_id uuid not null REFERENCES subject,
    teacher_id uuid not null REFERENCES teacher
);

CREATE UNIQUE INDEX subject_to_teacher_idx ON subject_to_teacher (subject_id, teacher_id);

create table if not exists hometask (
    id uuid primary key default uuid_generate_v4(),
    task text not null,
    lesson_id uuid not null REFERENCES lesson,
    created timestamp with time zone default current_timestamp
);

create table if not exists lesson_to_class (
    id uuid primary key default uuid_generate_v4(),
    class_id uuid not null REFERENCES class,
    lesson_id uuid not null REFERENCES lesson
);
